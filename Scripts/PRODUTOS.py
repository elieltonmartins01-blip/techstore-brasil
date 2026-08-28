import random
from datetime import date
import pandas as pd
from faker import Faker
fake = Faker()

# ==========================
# CONFIGURAÇÕES
# ==========================

QUANTIDADE_DE_PRODUTOS = 200
produtos = []

CATALOGO = {
    "Smartphones": [
        {"marca": "Samsung", "modelo": "Galaxy S24", "fornecedor": "Samsung"},
        {"marca": "Samsung", "modelo": "Galaxy A56", "fornecedor": "Samsung"},
        {"marca": "Samsung", "modelo": "Galaxy Z Flip6", "fornecedor": "Samsung"},
        {"marca": "Apple", "modelo": "iPhone 16", "fornecedor": "Apple"},
        {"marca": "Apple", "modelo": "iPhone 16 Pro", "fornecedor": "Apple"},
        {"marca": "Apple", "modelo": "iPhone 16 Pro Max", "fornecedor": "Apple"},
        {"marca": "Motorola", "modelo": "Edge 60", "fornecedor": "Motorola"},
        {"marca": "Motorola", "modelo": "Moto G85", "fornecedor": "Motorola"},
        {"marca": "Xiaomi", "modelo": "Redmi Note 14", "fornecedor": "Xiaomi"},
        {"marca": "Xiaomi", "modelo": "Poco X7", "fornecedor": "Xiaomi"}
    ],
    "Monitor": [
        {"marca": "LG", "modelo": "UltraGear 27", "fornecedor": "LG"},
        {"marca": "Samsung", "modelo": "Odyssey G5", "fornecedor": "Samsung"},
        {"marca": "Dell", "modelo": "P2422H", "fornecedor": "Dell"},
        {"marca": "LG", "modelo": "UltraWide 29", "fornecedor": "LG"}
    ],
    "Notebook": [
        {"marca": "Dell", "modelo": "Inspiron 15", "fornecedor": "Dell"},
        {"marca": "Dell", "modelo": "Latitude 5450", "fornecedor": "Dell"},
        {"marca": "Lenovo", "modelo": "IdeaPad 3", "fornecedor": "Lenovo"},
        {"marca": "Lenovo", "modelo": "ThinkPad E14", "fornecedor": "Lenovo"},
        {"marca": "Acer", "modelo": "Aspire 5", "fornecedor": "Acer"},
        {"marca": "ASUS", "modelo": "VivoBook 15", "fornecedor": "ASUS"}
    ]
}

ARMAZENAMENTO = ["64GB", "128GB", "256GB", "512GB"]

# ==========================
# PREÇO DOS PRODUTOS
# ==========================

FAIXA_PRECO = {
    "Smartphones": (1200, 9000),
    "Monitor": (700, 4500),
    "Notebook": (2800, 12000)
}

# ==========================
# REGRAS DE CUSTO
# ==========================

FAIXA_CUSTO = {
    "Smartphones": (0.65, 0.80),
    "Monitor": (0.70, 0.85),
    "Notebook": (0.60, 0.75)
}

# ==========================
# ESTOQUE
# ==========================
    
FAIXA_ESTOQUE = {
    "Smartphones": (2, 80),
    "Monitor": (10, 40),
    "Notebook": (5, 30)
}

ATIVO = [True, False]

PESOS_ATIVO = [95, 5]



ANO = [2024, 2025, 2026]

PESOS_ANO = [20, 50, 30]

            
# ==========================
# 1. GERANDO O POOL DE TODAS AS COMBINAÇÕES POSSÍVEIS
# ==========================
lista_combinacoes_base = []

for categoria, lista_produtos in CATALOGO.items():
    for produto in lista_produtos:
        if categoria == "Smartphones":
            # Para smartphones, gera uma combinação para cada tamanho de memória
            for espaco in ARMAZENAMENTO:
                item = produto.copy()
                item["categoria"] = categoria
                item["nome_produto"] = f"{produto['marca']} {produto['modelo']} {espaco}"
                lista_combinacoes_base.append(item)
        else:
            # Para monitores e notebooks, mantém o nome padrão
            item = produto.copy()
            item["categoria"] = categoria
            item["nome_produto"] = f"{produto['marca']} {produto['modelo']}"
            lista_combinacoes_base.append(item)

# ==========================
# 2. GERANDO OS 200 PRODUTOS ÚNICOS
# ==========================


bases_sorteadas = random.choices(lista_combinacoes_base, k=QUANTIDADE_DE_PRODUTOS)

for i, produto_base in enumerate(bases_sorteadas, start=1):
    categoria_escolhida = produto_base["categoria"]
    
   
    nome_exclusivo = f"{produto_base['nome_produto']} (Lote #{i:03d})"
    
    
    preco_min, preco_max = FAIXA_PRECO[categoria_escolhida]
    preco = round(random.uniform(preco_min, preco_max), 2)

    custo_min, custo_max = FAIXA_CUSTO[categoria_escolhida]
    percentual_custo = random.uniform(custo_min, custo_max)
    custo = round(preco * percentual_custo, 2)

    estoque_min, estoque_max = FAIXA_ESTOQUE[categoria_escolhida]
    estoque = random.randint(estoque_min, estoque_max)

  
    ativo = random.choices(ATIVO, weights=PESOS_ATIVO, k=1)[0]
    ano = random.choices(ANO, weights=PESOS_ANO, k=1)[0]

   
    novo_produto = {
        "nome_produto": nome_exclusivo,
        "categoria": categoria_escolhida,
        "marca": produto_base["marca"],
        "fornecedor": produto_base["fornecedor"],
        "preco": preco,
        "custo": custo,
        "estoque": estoque,
        "ativo": ativo,
        "data_cadastro": fake.date_between(
            start_date=date(ano, 1, 1), 
            end_date=date(ano, 12, 30))
    }

    produtos.append(novo_produto)

# ==========================
# DATAFRAME E EXIBIÇÃO
# ==========================
df = pd.DataFrame(produtos)


print(df.head(15))


print(f"\nTotal de produtos gerados: {len(df)}")
print(f"Total de produtos com nomes únicos: {df['nome_produto'].nunique()}")
# ==========================
# EXPORTAÇÃO
# ==========================
import os

print(os.getcwd())

df = pd.DataFrame(produtos)
df.to_csv("produtos.csv", index=False, encoding="utf-8-sig")

print("Arquivo produtos.csv criado com sucesso!")
