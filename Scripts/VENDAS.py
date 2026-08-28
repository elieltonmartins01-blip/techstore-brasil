import random
from datetime import datetime, timedelta
import pandas as pd
import os


# ==========================
# CONFIGURAÇÕES
# ==========================

QUANTIDADE_VENDAS = 5000
PERIODO_DIAS = 365
DATA_INICIO = datetime.now() - timedelta(days=PERIODO_DIAS)
DATA_FIM = datetime.now()

# IDs existentes no banco
IDS_CLIENTES = list(range(1, 1000))
IDS_VENDEDORES = list(range(1, 50))
IDS_PAGAMENTOS = list(range(1, 7))
IDS_PRODUTOS = list(range(1, 201))

# ==========================
# FUNÇÕES
# ==========================

def gerar_data_venda():
    delta = DATA_FIM - DATA_INICIO
    random_dias = random.randint(0, delta.days)
    data = DATA_INICIO + timedelta(days=random_dias)
    hora = random.randint(9, 18)
    minuto = random.randint(0, 59)
    return data.replace(hour=hora, minute=minuto, second=0, microsecond=0)

def gerar_status(data_venda):
    """Define status baseado na data da venda"""
    dias_desde_venda = (datetime.now() - data_venda).days
    
    if dias_desde_venda <= 2:
        return random.choices(
            ['Pendente', 'Pago', 'Enviado', 'Entregue'],
            weights=[0.30, 0.30, 0.25, 0.15]
        )[0]
    elif dias_desde_venda <= 5:
        return random.choices(
            ['Pendente', 'Pago', 'Enviado', 'Entregue'],
            weights=[0.10, 0.20, 0.30, 0.40]
        )[0]
    elif dias_desde_venda <= 10:
        return random.choices(
            ['Pendente', 'Pago', 'Enviado', 'Entregue'],
            weights=[0.05, 0.10, 0.15, 0.70]
        )[0]
    else:
        return random.choices(
            ['Pendente', 'Pago', 'Enviado', 'Entregue', 'Cancelado'],
            weights=[0.02, 0.03, 0.05, 0.85, 0.05]
        )[0]

def selecionar_cliente():
    return random.choice(IDS_CLIENTES)

def selecionar_vendedor():
    return random.choice(IDS_VENDEDORES)

def selecionar_pagamento(valor_total):
    if valor_total > 1000:
        pesos = [0.10, 0.60, 0.10, 0.05, 0.05, 0.10]
    elif valor_total > 500:
        pesos = [0.15, 0.40, 0.15, 0.10, 0.10, 0.10]
    else:
        pesos = [0.30, 0.20, 0.20, 0.10, 0.10, 0.10]
    return random.choices(IDS_PAGAMENTOS, weights=pesos)[0]

def gerar_preco_produto(id_produto):
    # Dicionário com preços para alguns produtos
    precos_base = {
        1: 4500.00, 2: 6200.00, 3: 2500.00, 4: 3800.00, 5: 2200.00,
        6: 1500.00, 7: 800.00, 8: 1200.00, 9: 3500.00, 10: 1800.00,
        11: 500.00, 12: 700.00, 13: 900.00, 14: 300.00, 15: 250.00,
    }
    if id_produto in precos_base:
        return precos_base[id_produto]
    return round(random.uniform(50, 5000), 2)

def gerar_carrinho():
    num_itens = random.randint(1, 4)
    produtos_escolhidos = random.sample(IDS_PRODUTOS, num_itens)
    
    itens = []
    total = 0
    
    for id_produto in produtos_escolhidos:
        preco = gerar_preco_produto(id_produto)
        
        if preco > 2000:
            qtd = random.randint(1, 2)
        elif preco > 500:
            qtd = random.randint(1, 3)
        else:
            qtd = random.randint(1, 5)
        
        if qtd >= 3:
            desconto_percentual = random.choice([0, 0.05, 0.10])
        else:
            desconto_percentual = random.choice([0, 0, 0, 0.05])
        
        desconto_valor = round(preco * desconto_percentual * qtd, 2)
        subtotal = round((preco * (1 - desconto_percentual)) * qtd, 2)
        
        itens.append({
            'id_produto': id_produto,
            'quantidade': qtd,
            'valor_unitario': round(preco, 2),
            'desconto': desconto_valor
        })
        
        total += subtotal
    
    return itens, round(total, 2)


vendas = []
itens_venda = []

for i in range(QUANTIDADE_VENDAS):
    if (i + 1) % 500 == 0:
        print(f"  • Gerando venda {i+1}/{QUANTIDADE_VENDAS}")
    
    # Data da venda
    data_venda = gerar_data_venda()
    
    # Cliente
    id_cliente = selecionar_cliente()
    
    # Carrinho
    carrinho, total_venda = gerar_carrinho()
    
    # Vendedor
    id_vendedor = selecionar_vendedor()
    
    # Forma de pagamento
    id_pagamento = selecionar_pagamento(total_venda)
    
    # Status (GERADO AUTOMATICAMENTE)
    status = gerar_status(data_venda)
    
    # Criar venda (com status preenchido)
    venda = {
        'data_venda': data_venda.strftime('%Y-%m-%d %H:%M:%S'),
        'id_cliente': id_cliente,
        'id_vendedores': id_vendedor,
        'id_pagamentos': id_pagamento,
        'valor_total': total_venda,
        'status': status  # ← STATUS PREENCHIDO
    }
    vendas.append(venda)
    
    # Criar itens
    for item in carrinho:
        item['id_venda'] = i + 1
        itens_venda.append(item)

# ==========================
# CRIAR DATAFRAMES
# ==========================

df_vendas = pd.DataFrame(vendas)
df_itens = pd.DataFrame(itens_venda)



# ==========================
# SALVAR CSVs
# ==========================

CAMINHO = r"D:\PROJETO_PASTA\DADOS"
os.makedirs(CAMINHO, exist_ok=True)

df_vendas.to_csv(os.path.join(CAMINHO, "vendas.csv"), 
                 index=False, encoding='utf-8-sig')

colunas_itens = ['id_venda', 'id_produto', 'quantidade', 'valor_unitario', 'desconto']
df_itens[colunas_itens].to_csv(os.path.join(CAMINHO, "itens_venda.csv"),
                                index=False, encoding='utf-8-sig')

