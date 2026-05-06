"""Geração de relatórios em TXT e CSV."""
from __future__ import annotations

import csv
from pathlib import Path
from app.analyzer import ParsedLog


def generate_txt_report(output_path: str | Path, summary: dict, errors: list[ParsedLog]) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("RELATÓRIO DE ANÁLISE DE LOGS\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Total de linhas: {summary['total_lines']}\n")
        file.write(f"Logs válidos: {summary['valid_logs']}\n")
        file.write(f"Linhas inválidas: {summary['invalid_lines']}\n")
        file.write(f"Total de erros: {summary['total_errors']}\n")
        file.write(f"IPs únicos: {summary['unique_ips']}\n\n")

        file.write("RESUMO POR NÍVEL\n")
        file.write("-" * 60 + "\n")
        for level, total in summary["levels"].items():
            file.write(f"{level}: {total}\n")

        file.write("\nTOP IPS\n")
        file.write("-" * 60 + "\n")
        for ip, total in summary["top_ips"].items():
            file.write(f"{ip}: {total}\n")

        file.write("\nERROS ENCONTRADOS\n")
        file.write("-" * 60 + "\n")
        for error in errors[:100]:
            file.write(f"{error.log_date} | {error.log_level} | {error.ip_address or '-'} | {error.message}\n")


def export_csv(output_path: str | Path, logs: list[ParsedLog]) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["log_date", "log_level", "ip_address", "message"])
        for log in logs:
            writer.writerow([
                log.log_date.strftime("%Y-%m-%d %H:%M:%S"),
                log.log_level,
                log.ip_address or "",
                log.message,
            ])
