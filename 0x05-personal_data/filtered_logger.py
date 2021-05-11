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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ log formatter """
        letter = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            letter, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Create logger """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    hdlr = logging.StreamHandler()
    hdlr.setLevel(logging.INFO)
    formatter = RedactingFormatter(list(PII_FIELDS))
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    return logger