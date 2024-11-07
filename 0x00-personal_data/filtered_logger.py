#!/usr/bin/env python3
"""
Filtered Login Module
"""
from typing import List
import re
import logging


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
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Class Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filtered Message
        """
        logMessage = logging.Formatter(self.FORMAT).format(record)
        filtered_message = filter_datum(
            self.fields, self.REDACTION, logMessage, self.SEPARATOR
            )
        return filtered_message
