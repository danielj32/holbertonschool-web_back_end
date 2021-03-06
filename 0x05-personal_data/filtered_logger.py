#!/usr/bin/env python3
"""  Regex-ing """
import os
import re
import logging
from typing import List
import mysql.connector
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    connector = mysql.connector.connect(
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME"))
    return connector


def main():
    """ main
    principal """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        letter = "name={}; email={}; phone={}; ssn={}; password={};\
ip={}; last_login={}; user_agent={}; ".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )
        letter = filter_datum(list(PII_FIELDS), '***', letter, '; ')
        logger.info(letter)
    cursor.close()
    db.close()


if __name__ == '__main__':
    """ Only the main
    run when the module is executed """
    main()
