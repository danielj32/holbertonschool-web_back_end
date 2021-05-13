#!/usr/bin/env python3
""" class to manage
the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method auth """
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
        """ current method """
        return None
