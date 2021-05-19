#!/usr/bin/env python3
""" class to
authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method check
        if authorized """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] == '/' and path[:-1] in excluded_paths:
            return False
        if path in excluded_paths:
            return False
        if path[-1] != '/' and path + '/' in excluded_paths:
            return False
        for j in excluded_paths:
            if j[-1] == "*" and path.startswith(j[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ header auth """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ current method
        for user
        """
        return None

    def session_cookie(self, request=None):
        """ Method returns an
        cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
