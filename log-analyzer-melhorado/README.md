# 📊 Log Analyzer

Projeto em Python para análise de logs de sistema, com geração de relatórios, gráficos, exportação CSV, dashboard em Streamlit e integração opcional com MySQL.

## 🚀 Funcionalidades

- Leitura de arquivos `.log` e `.txt`
- Parsing profissional com Regex
- Contagem de logs por nível: `INFO`, `WARNING`, `ERROR`, `DEBUG`, `CRITICAL`
- Extração e contagem de IPs
- Identificação de erros
- Geração de gráfico em PNG
- Geração de relatório em TXT
- Exportação dos logs analisados para CSV
- Dashboard interativo com Streamlit
- Inserção opcional no MySQL
- Testes automatizados com Pytest
- Estrutura modular de projeto

## 🛠️ Tecnologias

- Python
- Regex
- Matplotlib
- Pandas
- Streamlit
- MySQL
- Pytest
- Git/GitHub

## 📁 Estrutura

```text
log-analyzer-melhorado/
│
├── app/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── charts.py
│   ├── config.py
│   ├── database.py
│   └── reports.py
│
├── charts/
├── database/
│   └── schema.sql
├── logs/
│   └── system.log
├── reports/
├── tests/
│   └── test_analyzer.py
│
├── dashboard.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Como rodar o projeto

### 1. Entrar na pasta

```bash
cd log-analyzer-melhorado
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar análise pelo terminal

```bash
python main.py
```

Depois disso, serão gerados:

```text
reports/report.txt
reports/logs_analisados.csv
charts/logs_por_nivel.png
```

### 5. Rodar dashboard

```bash
streamlit run dashboard.py
```

## 🗄️ Como usar com MySQL

### 1. Criar o banco

Abra o MySQL Workbench e execute o arquivo:

```text
database/schema.sql
```

Ou copie o conteúdo dele e rode no MySQL.

### 2. Criar o arquivo `.env`

Copie o arquivo `.env.example` e renomeie para `.env`.

Exemplo:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=logsystem
LOG_FILE=logs/system.log
```

### 3. Rodar salvando no banco

```bash
python main.py --save-db
```

## 🧪 Rodar testes

```bash
pytest
```

## 🔥 Melhorias futuras

- Login de usuários
- API REST com FastAPI
- Upload de vários arquivos ao mesmo tempo
- Filtros por intervalo de data
- Deploy do dashboard
- Docker
