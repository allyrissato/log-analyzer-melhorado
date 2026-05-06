# 📊 Log Analyzer

Sistema de análise automatizada de logs desenvolvido em Python com dashboard interativo em Streamlit.

O projeto foi criado com foco em observabilidade, monitoramento e análise de eventos de sistemas, permitindo identificar erros e gerar relatórios automaticamente.

---

# 🚀 Melhorias Implementadas

Este projeto passou por diversas melhorias para ficar mais profissional e próximo de sistemas reais utilizados em empresas.

## ✅ Estrutura Profissional

O projeto foi reorganizado em módulos:

```text
app/
logs/
reports/
charts/
tests/
```

Isso melhora:

* organização,
* manutenção,
* escalabilidade.

---

## ✅ Dashboard Web com Streamlit

Antes o sistema funcionava apenas no terminal.

Agora possui:

* dashboard web,
* gráficos,
* estatísticas,
* visual interativo.

---

## ✅ Parsing de Logs com Regex

O sistema agora utiliza Regex para interpretar logs de forma mais robusta.

Exemplo:

```python
re.match()
```

Isso permite identificar:

* INFO
* WARNING
* ERROR

---

## ✅ Geração de Relatórios

O projeto gera:

* relatórios TXT,
* exportação CSV,
* análises automáticas.

---

## ✅ Gráficos Automáticos

O sistema cria gráficos para visualizar:

* erros,
* warnings,
* informações,
* estatísticas gerais.

---

## ✅ Testes Automatizados

Foi adicionada uma pasta:

```text
tests/
```

Utilizando:

* Pytest

---

## ✅ Segurança e Organização

Adicionado:

* `.gitignore`
* `.env.example`
* separação modular
* limpeza de arquivos desnecessários

---

# 🖥️ Dashboard

![Dashboard](images/dashboard.png)

---

# 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Matplotlib
* Regex
* Pytest
* Git/GitHub

---

# 📂 Estrutura do Projeto

```text
log-analyzer/
│
├── app/
│   ├── analyzer.py
│   ├── charts.py
│   ├── reports.py
│   └── utils.py
│
├── logs/
├── charts/
├── reports/
├── tests/
├── images/
│
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEUUSUARIO/log-analyzer-dashboard.git
```

---

## 2️⃣ Entrar na pasta

```bash
cd log-analyzer-dashboard
```

---

## 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

Ativar ambiente:

```bash
venv\Scripts\activate
```

---

## 4️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executar Projeto

## Terminal

```bash
python main.py
```

---

## Dashboard Web

```bash
streamlit run dashboard.py
```

---

# 📄 Exemplo de Log

```text
2026-05-06 10:00:00 INFO Sistema iniciado
2026-05-06 10:01:15 WARNING CPU acima de 80%
2026-05-06 10:02:33 ERROR Falha ao conectar no banco
```

---

# 🎯 Objetivo do Projeto

Automatizar a análise de logs para facilitar identificação de erros, monitoramento de eventos e geração de estatísticas.

---

# 💼 Competências Demonstradas

Este projeto demonstra conhecimentos em:

* Python
* Regex
* Estruturação de projetos
* Streamlit
* Visualização de dados
* Automação
* Git/GitHub
* Manipulação de arquivos
* Dashboards interativos
* Testes automatizados

---

# 🚀 Melhorias Futuras

* Upload múltiplo de logs
* API REST com FastAPI
* Docker
* PostgreSQL
* Dashboard em tempo real
* Login de usuários
* Deploy em nuvem

---

# 👩‍💻 Desenvolvido por

Alianny Rissato
