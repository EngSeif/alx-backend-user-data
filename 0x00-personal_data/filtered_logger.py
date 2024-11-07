#!/usr/bin/env python3
"""
Filtered Login Module
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")
db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
db_name = os.getenv('PERSONAL_DATA_DB_NAME')


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns a connector to the database
    """
    try:
        connection = mysql.connector.connect(
                user=db_username,
                password=db_password,
                host=db_host,
                database=db_name
            )
        if connection.is_connected():
            return connection
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def get_logger() -> logging.Logger:
    """
    Logger Config
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter()
    stream_handler.setFormatter(formatter)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.
    """
    pattern = (
        r'(' + '|'.join(map(re.escape, fields)) + r')=' +
        r'([^' + re.escape(separator) + r']*)'
    )
    return re.sub(pattern, r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
