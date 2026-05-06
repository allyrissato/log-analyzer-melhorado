"""Ponto de entrada principal do projeto."""
from __future__ import annotations

import argparse
import logging
from pathlib import Path

from app.analyzer import LogAnalyzer, logs_to_rows
from app.charts import generate_level_chart
from app.config import Config
from app.database import DatabaseManager
from app.reports import export_csv, generate_txt_report

logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def ensure_directories() -> None:
    for folder in ["logs", "reports", "charts", "database"]:
        Path(folder).mkdir(exist_ok=True)


def run_analysis(log_file: str | Path, save_db: bool = False) -> dict:
    analyzer = LogAnalyzer(log_file)
    analyzer.load_logs()

    summary = analyzer.summary()
    errors = analyzer.find_errors()

    generate_level_chart(summary["levels"], Config.CHART_OUTPUT)
    generate_txt_report(Config.REPORT_OUTPUT, summary, errors)
    export_csv(Config.CSV_OUTPUT, analyzer.parsed_logs)

    if save_db:
        with DatabaseManager() as db:
            inserted = db.insert_batch(logs_to_rows(analyzer.parsed_logs))
            summary["db_inserted"] = inserted

    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Analisador de logs em Python")
    parser.add_argument("--file", default=str(Config.LOG_FILE), help="Caminho do arquivo .log")
    parser.add_argument("--save-db", action="store_true", help="Salvar logs no banco MySQL")
    args = parser.parse_args()

    ensure_directories()

    try:
        summary = run_analysis(args.file, save_db=args.save_db)
        logger.info("Análise concluída com sucesso!")
        logger.info("Resumo: %s", summary)
        return 0
    except FileNotFoundError as exc:
        logger.error(exc)
        return 1
    except Exception as exc:
        logger.exception("Erro inesperado: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
