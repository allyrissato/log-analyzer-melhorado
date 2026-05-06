# ✅ Melhorias realizadas no projeto Log Analyzer

## 1. README corrigido

O README antigo estava com conflito de Git, aparecendo marcações como:

```text
<<<<<<< HEAD
=======
>>>>>>> código
```

Essas marcações foram removidas e o README foi reescrito com uma estrutura profissional para GitHub.

---

## 2. Remoção de arquivos desnecessários

A nova versão não inclui:

- pasta `.git`
- arquivo `.env` real
- `__pycache__`
- arquivos temporários

Isso deixa o projeto mais seguro e limpo para enviar ao GitHub.

---

## 3. Estrutura reorganizada

Antes, os arquivos principais ficavam todos na raiz do projeto.

Agora o projeto foi organizado assim:

```text
app/
├── analyzer.py
├── charts.py
├── config.py
├── database.py
└── reports.py
```

Isso deixa o código mais profissional e fácil de manter.

---

## 4. Parser de logs melhorado com Regex

Antes, o projeto separava a linha usando `split`, o que poderia quebrar dependendo do formato do log.

Agora ele usa Regex para identificar:

- data
- horário
- nível do log
- mensagem
- IP

Exemplo de linha aceita:

```text
2024-05-03 10:30:45 ERROR IP=192.168.1.1 Erro crítico no sistema
```

---

## 5. Criação de classe ParsedLog

Foi criada uma estrutura com `dataclass` para representar cada log analisado.

Agora cada log possui:

- `log_date`
- `log_level`
- `message`
- `ip_address`
- `raw_line`

Isso deixa o projeto mais organizado.

---

## 6. Relatórios melhores

Agora o projeto gera:

```text
reports/report.txt
reports/logs_analisados.csv
```

O relatório mostra:

- total de linhas
- logs válidos
- linhas inválidas
- total de erros
- IPs únicos
- resumo por nível
- top IPs
- lista de erros

---

## 7. Gráfico melhorado

Agora o gráfico é salvo automaticamente em:

```text
charts/logs_por_nivel.png
```

Ele mostra a quantidade de logs por nível.

---

## 8. Dashboard com Streamlit

Foi criado o arquivo:

```text
dashboard.py
```

Com ele você pode abrir uma interface web para:

- enviar arquivo de log
- ver métricas
- ver gráfico
- filtrar por nível
- buscar palavra-chave
- visualizar tabela de logs

Para rodar:

```bash
streamlit run dashboard.py
```

---

## 9. Banco de dados melhorado

A tabela do MySQL agora possui mais campos:

```sql
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log_date DATETIME NOT NULL,
    log_level VARCHAR(20) NOT NULL,
    ip_address VARCHAR(50),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Foi adicionado:

- campo `ip_address`
- campo `created_at`
- `DATETIME` para a data
- `IF NOT EXISTS`

---

## 10. Inserção no banco ficou opcional

Agora o projeto pode rodar sem MySQL:

```bash
python main.py
```

E também pode salvar no banco quando você quiser:

```bash
python main.py --save-db
```

Isso evita erro para quem só quer testar o projeto localmente.

---

## 11. Testes automatizados

Foi criada a pasta:

```text
tests/
```

Com teste para validar o parser de logs.

Para rodar:

```bash
pytest
```

---

# ▶️ Passo a passo para usar

## 1. Abrir a pasta no VS Code

Abra a pasta:

```text
log-analyzer-melhorado
```

## 2. Abrir o terminal

No VS Code:

```text
Terminal > New Terminal
```

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

## 4. Ativar ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

## 6. Rodar pelo terminal

```bash
python main.py
```

## 7. Rodar dashboard

```bash
streamlit run dashboard.py
```

## 8. Rodar testes

```bash
pytest
```

---

# 💼 Como apresentar esse projeto

Você pode dizer:

> Esse projeto é um analisador de logs desenvolvido em Python. Ele lê arquivos de log, identifica níveis como ERROR, WARNING e INFO, extrai IPs, gera relatórios, gráficos e um dashboard interativo. Também possui integração opcional com MySQL e testes automatizados. Melhorei a arquitetura do código separando responsabilidades em módulos, usei Regex para deixar o parser mais robusto e adicionei exportação CSV para facilitar análises de dados.
