import random
from datetime import date
from faker import Faker
import pandas as pd

# ==========================
# CONFIGURAÇÕES
# ==========================

fake = Faker("pt_BR")
clientes = []

# ==========================
# ESTADOS E PROBABILIDADES (USANDO OS PESOS PARA UM DADO MAIS REAL)
# ==========================

ESTADOS = ["SP", "PR", "RJ", "MG", "SC", "RS", "GO", "BA"]
PESOS = [30, 30, 10, 10, 8, 6, 3, 3]

CIDADES = {
    "SP": ["São Paulo", "Campinas", "Santos", "Ribeirão Preto"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa"],
    "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis"],
    "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora"],
    "SC": ["Florianópolis", "Joinville", "Blumenau"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
    "GO": ["Goiânia", "Anápolis", "Rio Verde"],
    "BA": ["Salvador", "Feira de Santana", "Porto Seguro"]
}

# ==========================
# GERAÇÃO DOS DADOS
# ==========================

quantidade_de_clientes = 1000

for _ in range(quantidade_de_clientes):
    estado_escolhido = random.choices(ESTADOS, weights=PESOS, k=1)[0]
    cidade_escolhida = random.choice(CIDADES[estado_escolhido])

    cliente = {
        "nome": fake.name(),
        "cpf": fake.unique.cpf(),
        "email": fake.unique.email(),
        "telefone": fake.phone_number(),
        "cidade": cidade_escolhida,
        "estado": estado_escolhido,
        "sexo": random.choice(["M", "F"]),
        "idade": random.randint(18, 75),
        "data_cadastro": fake.date_between(
            start_date=date(2024, 1, 1), end_date=date(2026, 6, 30)
        ),
    }

    clientes.append(cliente)


# ==========================
# EXPORTAÇÃO
# ==========================
import os

print(os.getcwd())

df = pd.DataFrame(clientes)
df.to_csv("clientes.csv", index=False, encoding="utf-8-sig")

