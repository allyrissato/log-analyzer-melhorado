"""Dashboard interativo em Streamlit."""
from pathlib import Path
import tempfile

import pandas as pd
import streamlit as st

from app.analyzer import LogAnalyzer

st.set_page_config(page_title="Log Analyzer", page_icon="📊", layout="wide")

st.title("📊 Log Analyzer Dashboard")
st.write("Envie um arquivo `.log` ou use o arquivo de exemplo para visualizar a análise.")

uploaded_file = st.file_uploader("Enviar arquivo de log", type=["log", "txt"])

if uploaded_file:
    temp_path = Path(tempfile.gettempdir()) / uploaded_file.name
    temp_path.write_bytes(uploaded_file.getvalue())
    log_path = temp_path
else:
    log_path = Path("logs/system.log")

if log_path.exists():
    analyzer = LogAnalyzer(log_path)
    analyzer.load_logs()
    summary = analyzer.summary()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Linhas", summary["total_lines"])
    col2.metric("Logs válidos", summary["valid_logs"])
    col3.metric("Erros", summary["total_errors"])
    col4.metric("IPs únicos", summary["unique_ips"])

    st.subheader("Logs por nível")
    level_df = pd.DataFrame(summary["levels"].items(), columns=["Nível", "Quantidade"])
    st.bar_chart(level_df.set_index("Nível"))

    rows = [
        {
            "Data": log.log_date,
            "Nível": log.log_level,
            "IP": log.ip_address,
            "Mensagem": log.message,
        }
        for log in analyzer.parsed_logs
    ]
    df = pd.DataFrame(rows)

    st.subheader("Filtros")
    levels = ["Todos"] + sorted(df["Nível"].dropna().unique().tolist()) if not df.empty else ["Todos"]
    selected_level = st.selectbox("Filtrar por nível", levels)
    keyword = st.text_input("Buscar palavra na mensagem")

    filtered = df.copy()
    if selected_level != "Todos":
        filtered = filtered[filtered["Nível"] == selected_level]
    if keyword:
        filtered = filtered[filtered["Mensagem"].str.contains(keyword, case=False, na=False)]

    st.subheader("Tabela de logs")
    st.dataframe(filtered, use_container_width=True)
else:
    st.error("Arquivo de log não encontrado.")
