import random
import pandas as pd
from pathlib import Path
from datetime import datetime

# ==========================
# CONFIGURAÇÕES
# ==========================

TOTAL_VENDAS = 5000
CAMINHO_DADOS = Path(r"D:\PROJETO_PASTA\DADOS")
TOTAL_PRODUTOS = 200
SEED = 42

# ==========================
# PREÇOS DOS PRODUTOS
# ==========================

PRECOS = {
    1: 4500.00, 2: 6200.00, 3: 2800.00, 4: 3500.00, 5: 8000.00,
    6: 1200.00, 7: 1500.00, 8: 900.00, 9: 2500.00, 10: 1800.00,
    11: 3800.00, 12: 4500.00, 13: 5500.00, 14: 6500.00, 15: 12000.00,
    16: 2800.00, 17: 3200.00, 18: 4000.00, 19: 5000.00, 20: 7000.00,
    21: 1500.00, 22: 2200.00, 23: 2500.00, 24: 3500.00, 25: 1800.00,
    26: 900.00, 27: 1200.00, 28: 800.00, 29: 1000.00, 30: 2800.00,
    31: 3500.00, 32: 5500.00, 33: 8000.00, 34: 4000.00, 35: 6000.00,
    36: 2500.00, 37: 3000.00,
    38: 3500.00, 39: 5000.00, 40: 2500.00, 41: 4000.00, 42: 6000.00,
    43: 1800.00, 44: 2200.00, 45: 1500.00,
    46: 2500.00, 47: 3500.00, 48: 4000.00, 49: 5000.00, 50: 1200.00,
    51: 800.00, 52: 600.00, 53: 350.00, 54: 250.00,
    55: 800.00, 56: 600.00, 57: 450.00, 58: 300.00, 59: 250.00,
    60: 180.00, 61: 120.00, 62: 90.00, 63: 70.00, 64: 50.00,
    65: 350.00, 66: 280.00, 67: 200.00, 68: 150.00,
    69: 1500.00, 70: 1200.00, 71: 2500.00, 72: 3500.00, 73: 800.00,
    74: 600.00, 75: 450.00, 76: 300.00, 77: 200.00, 78: 150.00,
    79: 350.00, 80: 550.00, 81: 750.00, 82: 1200.00, 83: 450.00,
    84: 250.00, 85: 150.00, 86: 100.00, 87: 80.00, 88: 60.00,
    89: 500.00, 90: 800.00, 91: 350.00, 92: 250.00, 93: 180.00,
    94: 2500.00, 95: 3500.00, 96: 4500.00, 97: 1800.00, 98: 2800.00,
    99: 3800.00, 100: 500.00, 101: 800.00, 102: 300.00, 103: 450.00,
    104: 600.00, 105: 850.00, 106: 1200.00, 107: 150.00, 108: 200.00,
    109: 2500.00, 110: 3500.00, 111: 4500.00, 112: 1800.00, 113: 800.00,
    114: 600.00, 115: 400.00, 116: 300.00, 117: 200.00, 118: 150.00,
    119: 800.00, 120: 1200.00, 121: 1500.00, 122: 600.00, 123: 400.00,
    124: 250.00, 125: 350.00,
    126: 3500.00, 127: 5500.00, 128: 4500.00, 129: 2800.00, 130: 1800.00,
    131: 1200.00, 132: 800.00,
    133: 450.00, 134: 650.00, 135: 850.00, 136: 1200.00, 137: 250.00,
    138: 180.00, 139: 300.00, 140: 200.00,
    141: 150.00, 142: 250.00, 143: 100.00, 144: 80.00, 145: 50.00,
    146: 30.00, 147: 45.00, 148: 60.00, 149: 90.00, 150: 120.00,
}


# ==========================
# FUNÇÕES
# ==========================

random.seed(SEED)
produtos = list(range(1, TOTAL_PRODUTOS + 1))

def get_preco(produto_id):
    return PRECOS.get(produto_id, round(random.uniform(50, 5000), 2))


itens_venda = []

for id_venda in range(1, TOTAL_VENDAS + 1):
    # Cada venda tem entre 1 e 4 produtos
    num_itens = random.randint(1, 4)
    produtos_escolhidos = random.sample(produtos, num_itens)
    
    for produto_id in produtos_escolhidos:
        preco = get_preco(produto_id)
        
        # Quantidade baseada no preço
        if preco > 2000:
            quantidade = random.randint(1, 2)
        elif preco > 500:
            quantidade = random.randint(1, 3)
        else:
            quantidade = random.randint(1, 5)
        
        # Desconto baseado na quantidade
        if quantidade >= 3:
            desconto_percent = random.choice([0, 0.05, 0.10, 0.15])
        else:
            desconto_percent = random.choice([0, 0, 0, 0.05])
        
        # Calcular valores
        valor_unitario = round(preco, 2)
        desconto = round(preco * desconto_percent * quantidade, 2)
        subtotal = round((preco * (1 - desconto_percent)) * quantidade, 2)
        
        # Adicionar item (COM SUBTOTAL)
        itens_venda.append({
            'id_venda': id_venda,
            'id_produto': produto_id,
            'quantidade': quantidade,
            'valor_unitario': valor_unitario,
            'desconto': desconto,
            'subtotal': subtotal  # ← SUBTOTAL CALCULADO
        })

# ==========================
# CRIAR DATAFRAME
# ==========================

df = pd.DataFrame(itens_venda)



# ==========================
# EXPORTAR CSV
# ==========================

CAMINHO_DADOS.mkdir(parents=True, exist_ok=True)
arquivo = CAMINHO_DADOS / "itens_venda.csv"
df.to_csv(arquivo, index=False, encoding='utf-8-sig')

print(f"\n📁 Arquivo salvo em: {arquivo}")

