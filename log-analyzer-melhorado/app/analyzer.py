"""Funções e classe para análise de arquivos de log."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
from typing import Iterable


LOG_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>ERROR|WARNING|INFO|DEBUG|CRITICAL)\s+"
    r"(?P<message>.*)$"
)

IP_PATTERN = re.compile(r"\b(?:IP=)?(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\b")


@dataclass
class ParsedLog:
    """Representa uma linha de log já interpretada."""
    log_date: datetime
    log_level: str
    message: str
    ip_address: str | None = None
    raw_line: str = ""


class LogAnalyzer:
    """Analisador de logs com parsing por Regex e resumo estatístico."""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        self.raw_lines: list[str] = []
        self.parsed_logs: list[ParsedLog] = []
        self.invalid_lines: list[str] = []

    def load_logs(self) -> None:
        """Carrega o arquivo e interpreta as linhas válidas."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        self.raw_lines = self.file_path.read_text(encoding="utf-8").splitlines()
        self.parsed_logs = []
        self.invalid_lines = []

        for line in self.raw_lines:
            parsed = self.parse_line(line)
            if parsed:
                self.parsed_logs.append(parsed)
            elif line.strip():
                self.invalid_lines.append(line)

    @staticmethod
    def parse_line(line: str) -> ParsedLog | None:
        """Transforma uma linha de texto em ParsedLog, se ela estiver no formato esperado."""
        match = LOG_PATTERN.match(line.strip())
        if not match:
            return None

        log_datetime = datetime.strptime(
            f"{match.group('date')} {match.group('time')}",
            "%Y-%m-%d %H:%M:%S",
        )
        message = match.group("message").strip()
        ip_match = IP_PATTERN.search(message)

        return ParsedLog(
            log_date=log_datetime,
            log_level=match.group("level"),
            message=message,
            ip_address=ip_match.group("ip") if ip_match else None,
            raw_line=line.strip(),
        )

    def count_levels(self) -> Counter:
        """Conta quantos logs existem por nível."""
        return Counter(log.log_level for log in self.parsed_logs)

    def extract_ips(self) -> Counter:
        """Conta ocorrências de IPs encontrados nas mensagens."""
        return Counter(log.ip_address for log in self.parsed_logs if log.ip_address)

    def find_errors(self) -> list[ParsedLog]:
        """Retorna logs do tipo ERROR ou CRITICAL."""
        return [log for log in self.parsed_logs if log.log_level in {"ERROR", "CRITICAL"}]

    def find_by_level(self, level: str) -> list[ParsedLog]:
        """Filtra logs por nível."""
        level = level.upper().strip()
        return [log for log in self.parsed_logs if log.log_level == level]

    def search(self, keyword: str) -> list[ParsedLog]:
        """Busca logs contendo uma palavra-chave na mensagem."""
        keyword = keyword.lower().strip()
        return [log for log in self.parsed_logs if keyword in log.message.lower()]

    def summary(self) -> dict:
        """Retorna um resumo geral da análise."""
        errors = self.find_errors()
        ips = self.extract_ips()
        return {
            "total_lines": len(self.raw_lines),
            "valid_logs": len(self.parsed_logs),
            "invalid_lines": len(self.invalid_lines),
            "total_errors": len(errors),
            "unique_ips": len(ips),
            "levels": dict(self.count_levels()),
            "top_ips": dict(ips.most_common(5)),
        }


def logs_to_rows(logs: Iterable[ParsedLog]) -> list[tuple]:
    """Converte ParsedLog para tuplas úteis em banco, CSV e relatórios."""
    return [
        (
            log.log_date.strftime("%Y-%m-%d %H:%M:%S"),
            log.log_level,
            log.ip_address,
            log.message,
        )
        for log in logs
    ]
