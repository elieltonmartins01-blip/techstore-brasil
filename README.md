# 🏪 TechStore Brasil - Dashboard de Vendas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)

> 📊 **Dashboard interativo de vendas** desenvolvido para a loja fictícia TechStore Brasil, com análise de faturamento, ticket médio e desempenho de produtos, categorias e vendedores.

![Dashboard](prints/dashboard.png)

---

## 📊 Sobre o Projeto

A **TechStore Brasil** é uma loja fictícia de tecnologia criada para simular um cenário real de análise de dados e apoiar a demonstração de um fluxo completo de Business Intelligence.
O projeto tem como objetivo transformar dados de vendas em indicadores e insights de negócio, permitindo analisar o desempenho comercial por meio de métricas como faturamento, quantidade de pedidos, ticket médio, produtos, categorias e vendedores.
A solução utiliza **Python** para geração dos dados, **MySQL** para armazenamento, **SQL** para consultas, **Power Query** para tratamento e preparação dos dados e **Power BI** para modelagem, análise e visualização dos indicadores.

## 🛠️ Tecnologias e Ferramentas

- 🐍 **Python** — Geração de dados fictícios
- 🗄️ **MySQL** — Armazenamento e gerenciamento do banco de dados
- 🔎 **SQL** — Consultas e análise dos dados
- 🔄 **Power Query** — Tratamento e preparação dos dados
- 📊 **Power BI** — Modelagem, criação de medidas e visualização
- 📁 **Git & GitHub** — Versionamento e documentação

---
## 🔄 Pipeline de Dados

```text
🐍 Python
   ↓
📦 Geração dos dados
   ↓
🗄️ MySQL
   ↓
🔎 Consultas SQL
   ↓
🔄 Power Query
   ↓
🧹 Tratamento dos dados
   ↓
📊 Power BI
   ↓
📈 Dashboard
   ↓
💡 Insights de Negócio
```
---
## 📈 Principais Indicadores

| Indicador | Valor |
|-----------|-------|
| **Faturamento Total** | R$ 146,13 Mi |
| **Total de Pedidos** | 15.000 |
| **Ticket Médio** | R$ 9.742,00 |
| **Produto Mais Vendido** | Inspiron Plus |
| **Unidades Vendidas** | 53.000 |


---
## 📁 Estrutura do Projeto

```text
techstore-brasil/
│
├── dashboard/              ← Arquivo do Power BI
│   └── Techstore_Brasil.pbix
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

## 💡 Principais Insights de Negócio

### 📈 Evolução do faturamento

Foi observada uma tendência de crescimento do faturamento ao longo do período analisado, com destaque para novembro de 2025.

### 🏷️ Desempenho por categoria

Notebooks apresentaram o maior faturamento entre as categorias analisadas, seguidos por Smartphones e Monitores.

### 🏆 Desempenho de produtos

O Inspiron Plus apresentou o maior volume de unidades vendidas entre os produtos analisados.

---
## 🎯 Análises Disponíveis

O dashboard permite acompanhar:

- Evolução do faturamento ao longo do tempo
- Desempenho de vendas por categoria
- Produtos com maior volume de vendas
- Desempenho dos vendedores
- Quantidade de pedidos
- Ticket médio
- Volume de unidades vendidas

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/elieltonmartins01-blip/techstore-brasil.git
cd techstore-brasil

```

### 2. Importar dados para o MySQL
```bash
mysql -u root -p techstore_brasil < sql/techstore_brasil_structure.sql

```
**Observação:** O projeto utiliza o Power Query para etapas de tratamento e preparação dos dados antes da análise no Power BI.
---

### 3. Abrir o dashboard no Power BI
- Abrir o arquivo `dashboard/Techstore_Brasil.pbix`
- Atualizar a conexão com o banco de dados
- **Pré-requisito:** Power BI Desktop instalado (download gratuito)

---
## 📚 Aprendizados

O desenvolvimento deste projeto permitiu praticar:

- Estruturação e modelagem de bancos de dados
- Consultas SQL aplicadas à análise de dados
- Geração e organização de dados com Python
- Tratamento de dados utilizando Power Query
- Criação de medidas e KPIs com DAX
- Construção de dashboards orientados a indicadores de negócio
- Documentação e versionamento utilizando Git e GitHub
  
---
## 📝 Licença

Este projeto é de uso livre para fins educacionais e de portfólio.

---

## 📬 Vamos Conectar

Fique à vontade para entrar em contato comigo para feedbacks, dúvidas ou oportunidades:

- 💼 LinkedIn: [Elielton Martins](https://www.linkedin.com/in/elielton-martins/)
- 🐙 GitHub: [elieltonmartins01-blip](https://github.com/elieltonmartins01-blip)
-📧 E-mail: elieltonmartins01@gmail.com

---

⭐ Se você gostou deste projeto, deixe uma estrela no repositório!
