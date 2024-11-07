#!/usr/bin/env python3
"""
Filtered Login Module
"""
from typing import List
import re


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
