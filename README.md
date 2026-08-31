# 🏪 TechStore Brasil - Dashboard de Vendas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)

> 📊 **Dashboard interativo de vendas** desenvolvido para a loja fictícia TechStore Brasil, com análise de faturamento, ticket médio e performance de produtos e vendedores.

![Dashboard](prints/dashboard.png)

---

## 📊 Sobre o Projeto

Dashboard de vendas desenvolvido para a loja fictícia **TechStore Brasil**, como parte do meu portfólio de análise de dados.

**Objetivo:** Demonstrar habilidades em:
- 🗄️ Modelagem de dados (MySQL)
- 🐍 Análise de dados (Python)
- 📊 Visualização de dados (Power BI)
- 🎨 Criação de dashboards interativos

---

## 📈 Principais Indicadores

| Indicador | Valor |
|-----------|-------|
| **Faturamento Total** | R$ 146,13 Mi |
| **Total de Pedidos** | 15.000 |
| **Ticket Médio** | R$ 9,74 Mi |
| **Produto Mais Vendido** | Inspiron Plus |
| **Unidades Vendidas** | 53.000 |

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python** - Geração de dados fictícios
- 🗄️ **MySQL** - Banco de dados
- 📊 **Power BI** - Dashboard e visualizações
- 📁 **Git & GitHub** - Controle de versão

---

## 📁 Estrutura do Projeto

```text
techstore-brasil/
│
├── dashboard/              ← Arquivo do Power BI
│   └── PROJETO.pbix
│
├── prints/                 ← Prints do dashboard
│   └── dashboard.png
│
├── scripts/                ← Scripts Python
│   ├── clientes.py
│   ├── produtos.py
│   └── vendas.py
│
├── sql/                    ← Scripts SQL
│   └── techstore_brasil_structure.sql
│
└── README.md               ← Documentação
```

## 🎯 Insights do Dashboard

### 📈 Evolução do Faturamento
- **Tendência de crescimento** ao longo do período
- **Pico de vendas** em nov/2025 (Black Friday) e jan/2026 (férias)
- **Ticket médio** de R$ 9,74 Mi

### 🏷️ Categorias com Maior Faturamento
1. **Notebook** - R$ 45 Mi
2. **Smartphone** - R$ 35 Mi
3. **Monitor** - R$ 25 Mi

### 🏆 Top 5 Produtos
1. Inspiron Plus - 2.500 unidades
2. G Pro Pro 32GB - 2.200 unidades
3. Redmi Note Ultra - 1.800 unidades
4. Virtuoso Pro - 1.500 unidades
5. Kumara Pro - 1.200 unidades

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/elieltonmartins01-blip/techstore-brasil.git

```

### 2. Importar dados para o MySQL
```bash
mysql -u root -p techsore_brasil < sql/techsore_brasil_structure.sql
```

### 3. Abrir o dashboard no Power BI
- Abrir o arquivo `dashboard/PROJETO.pbix`
- Atualizar a conexão com o banco de dados
- **Pré-requisito:** Power BI Desktop instalado (download gratuito)

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais e de portfólio.

---

## 📬 Vamos Conectar

Fique à vontade para entrar em contato comigo para feedbacks, dúvidas ou oportunidades:

- LinkedIn: [Elielton Martins](https://www.linkedin.com/in/elielton-martins/)
- GitHub: [elieltonmartins01-blip](https://github.com/elieltonmartins01-blip)
- E-mail: elieltonmartins01@gmail.com

---

⭐ Se você gostou deste projeto, deixe uma estrela no repositório!
