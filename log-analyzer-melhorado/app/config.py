"""Configurações centralizadas do projeto."""
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "logsystem")

    LOG_FILE = Path(os.getenv("LOG_FILE", BASE_DIR / "logs" / "system.log"))
    CHART_OUTPUT = Path(os.getenv("CHART_OUTPUT", BASE_DIR / "charts" / "logs_por_nivel.png"))
    REPORT_OUTPUT = Path(os.getenv("REPORT_OUTPUT", BASE_DIR / "reports" / "report.txt"))
    CSV_OUTPUT = Path(os.getenv("CSV_OUTPUT", BASE_DIR / "reports" / "logs_analisados.csv"))

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ALLOWED_LEVELS = {"ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL"}
