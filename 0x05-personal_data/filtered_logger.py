#!/usr/bin/env python3
"""  Regex-ing """
import os
import re
import logging
from typing import List
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """  returns the log message obfuscated """
    for i in fields:
        message = re.sub(fr"{i}=.+?{separator}",
                         f'{i}={redaction}{separator}', message)
    return message
