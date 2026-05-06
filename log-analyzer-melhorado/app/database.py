"""Camada de acesso ao banco MySQL."""
from __future__ import annotations

import logging
from typing import Iterable

try:
    import mysql.connector
    from mysql.connector import Error
except ModuleNotFoundError:  # permite rodar o projeto sem MySQL instalado
    mysql = None
    Error = Exception

from app.config import Config

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Gerencia conexão e inserção de logs no MySQL."""

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self) -> bool:
        if mysql is None:
            logger.warning("Pacote mysql-connector-python não instalado. Instale com: pip install mysql-connector-python")
            return False
        try:
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
            )
            self.cursor = self.connection.cursor()
            return True
        except Error as exc:
            logger.warning("Não foi possível conectar ao MySQL: %s", exc)
            return False

    def insert_batch(self, logs: Iterable[tuple]) -> int:
        """Insere vários logs de uma vez."""
        logs = list(logs)
        if not logs or not self.cursor:
            return 0

        sql = """
            INSERT INTO logs (log_date, log_level, ip_address, message)
            VALUES (%s, %s, %s, %s)
        """
        try:
            self.cursor.executemany(sql, logs)
            self.connection.commit()
            return self.cursor.rowcount
        except Error as exc:
            logger.error("Erro ao inserir logs: %s", exc)
            self.connection.rollback()
            return 0

    def close(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()
