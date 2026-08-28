import random
from datetime import datetime, timedelta, date
from faker import Faker
import pandas as pd
import os

# ==========================
# CONFIGURAÇÕES INICIAIS
# ==========================

fake = Faker("pt_BR")
Faker.seed(42)  # Para resultados reproduzíveis


# ==========================
# CONFIGURAÇÕES
# ==========================

QUANTIDADE_VENDEDORES = 50  # Quantos vendedores você quer gerar

# Estados e cidades (baseado no seu código de clientes)
ESTADOS = ["SP", "PR", "RJ", "MG", "SC", "RS", "GO", "BA"]
PESOS = [30, 30, 10, 10, 8, 6, 3, 3]  # Probabilidade de cada estado

CIDADES = {
    "SP": ["São Paulo", "Campinas", "Santos", "Ribeirão Preto", "Sorocaba", "São José dos Campos"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel", "Foz do Iguaçu"],
    "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis", "Duque de Caxias", "Nova Iguaçu"],
    "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora", "Contagem", "Betim"],
    "SC": ["Florianópolis", "Joinville", "Blumenau", "Itajaí", "São José"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Canoas", "Santa Maria"],
    "GO": ["Goiânia", "Anápolis", "Rio Verde", "Aparecida de Goiânia"],
    "BA": ["Salvador", "Feira de Santana", "Porto Seguro", "Vitória da Conquista"]
}

# Faixas de salário por região (mais realista)
SALARIO_MIN = 2500
SALARIO_MAX = 8000

# Faixa de comissão (%)
COMISSAO_MIN = 1.0
COMISSAO_MAX = 5.0


# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def gerar_telefone():
    """Gera um telefone brasileiro com DDD"""
    ddd = random.choice(['11', '12', '13', '14', '15', '16', '17', '18', '19',
                         '21', '22', '24', '27', '28', '31', '32', '33', '34',
                         '35', '37', '38', '41', '42', '43', '44', '45', '46',
                         '47', '48', '49', '51', '53', '54', '55', '61', '62',
                         '63', '64', '65', '66', '67', '68', '69', '71', '73',
                         '74', '75', '77', '79', '81', '82', '83', '84', '85',
                         '86', '87', '88', '89', '91', '92', '93', '94', '95',
                         '96', '97', '98', '99'])
    numero = f"{random.randint(9, 9)}{random.randint(0000, 9999):04d}{random.randint(0000, 9999):04d}"
    return f"{ddd}{numero}"

def gerar_email(nome):
    """Gera email baseado no nome"""
    # Remove acentos e caracteres especiais
    nome_limpo = nome.lower().replace(' ', '.').replace('ç', 'c').replace('ã', 'a')
    nome_limpo = ''.join(c for c in nome_limpo if c.isalnum() or c == '.')
    
    dominios = ['techstore.com.br', 'vendas.techstore.com.br', 'techstore.com', 'loja.techstore.com.br']
    dominio = random.choice(dominios)
    
    return f"{nome_limpo}@{dominio}"

def gerar_data_admissao():
    """Gera data de admissão entre 2020 e 2026"""
    ano = random.choices([2020, 2021, 2022, 2023, 2024, 2025, 2026], 
                         weights=[5, 10, 15, 25, 25, 15, 5])[0]
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    return date(ano, mes, dia)

def gerar_salario(estado):
    """Gera salário baseado no estado (custo de vida)"""
    # Ajuste por região
    if estado in ['SP', 'RJ']:
        multiplicador = random.uniform(1.1, 1.4)
    elif estado in ['PR', 'SC', 'RS']:
        multiplicador = random.uniform(0.9, 1.1)
    else:
        multiplicador = random.uniform(0.7, 0.9)
    
    salario_base = random.uniform(SALARIO_MIN, SALARIO_MAX)
    return round(salario_base * multiplicador, 2)

# GERAR VENDEDORES
# ==========================

print("\n🔄 Gerando vendedores...")

vendedores = []

for i in range(QUANTIDADE_VENDEDORES):
    # Nome
    nome = fake.name()
    
    # Estado (com peso)
    estado = random.choices(ESTADOS, weights=PESOS, k=1)[0]
    
    # Cidade
    cidade = random.choice(CIDADES[estado])
    
    # Email
    email = gerar_email(nome)
    
    # Telefone
    telefone = gerar_telefone()
    
    # Data de Admissão
    data_admissao = gerar_data_admissao()
    
    # Salário (baseado no estado)
    salario = gerar_salario(estado)
    
    # Comissão (baseada no salário)
    comissao = gerar_comissao(estado, salario)
    
    vendedor = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'cidade': cidade,
        'estado': estado,
        'data_admissao': data_admissao.strftime('%Y-%m-%d'),
        'salario': salario,
        'comissao': comissao
    }
    
    vendedores.append(vendedor)

print(f"\n✅ {len(vendedores)} vendedores gerados com sucesso!")

# ==========================
# CRIAR DATAFRAME
# ==========================

df = pd.DataFrame(vendedores)



# ==========================
# EXPORTAR PARA CSV
# ==========================

CAMINHO_DADOS = r"D:\PROJETO_PASTA\DADOS"

# Criar pasta se não existir
os.makedirs(CAMINHO_DADOS, exist_ok=True)

caminho_arquivo = os.path.join(CAMINHO_DADOS, "vendedores.csv")

df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')



sql_script = f"""
-- =====================================================
-- IMPORTAR VENDEDORES - TECHSTORE BRASIL
-- =====================================================

-- Verificar configuração de importação
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;

-- IMPORTAR VENDEDORES
LOAD DATA LOCAL INFILE '{CAMINHO_DADOS.replace('\\', '/')}/vendedores.csv'
INTO TABLE vendedores
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 ROWS
(nome, email, telefone, cidade, estado, data_admissao, salario, comissao);

-- VERIFICAR DADOS IMPORTADOS
SELECT 
    COUNT(*) as total_vendedores,
    AVG(salario) as media_salarial,
    AVG(comissao) as media_comissao
FROM vendedores;

SELECT 
    estado,
    COUNT(*) as quantidade,
    AVG(salario) as salario_medio
FROM vendedores
GROUP BY estado
ORDER BY quantidade DESC;
"""

# Salvar script SQL
caminho_sql = os.path.join(CAMINHO_DADOS, "importar_vendedores.sql")
with open(caminho_sql, 'w', encoding='utf-8') as f:
    f.write(sql_script)

print(f"✅ Script SQL salvo em: {caminho_sql}")
print(sql_script)

print("\n" + "="*60)
print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
print("="*60)

print("\n📋 PRÓXIMOS PASSOS:")
print("1. Execute o script SQL 'importar_vendedores.sql' no MySQL Workbench")
print("2. Verifique os dados com as queries de validação")
print("3. Conecte o Power BI ao banco de dados")
