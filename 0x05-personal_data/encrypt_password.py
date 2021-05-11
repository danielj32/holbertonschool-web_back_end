#!/usr/bin/env python3
"""Encode passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes encode string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if password is right"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
