#!/usr/bin/env python3
""" Basic auth
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ class BasicAuth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that
        the returns the Base64
        """
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        head = authorization_header.split(' ')

        return head[1] if head[0] == 'Basic' else None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value
        of to Base64
        base64_authorization_header
        """
        if (
           not base64_authorization_header or
           not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode(
                'utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns  user email
        and password from
        the Base64 decoded
        """
        if (
           not decoded_base64_authorization_header or
           not isinstance(decoded_base64_authorization_header, str) or
           ':' not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns of the User
        instance based on
        his email, password """
        if (
           not user_email or
           not isinstance(user_email, str) or
           not user_pwd or
           not isinstance(user_pwd, str)
           ):
            return None
        objs = User().search({"email": user_email})
        if not objs:
            return None
        if objs[0].is_valid_password(user_pwd):
            return objs[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """the overloads Auth
        and
        retrieves to the User
        instance
        for a request """
        if not request:
            return None
        auth_header = Auth().authorization_header(request)
        auth_header = self.extract_base64_authorization_header(auth_header)
        dec_header = self.decode_base64_authorization_header(auth_header)
        cred = self.extract_user_credentials(dec_header)
        return self.user_object_from_credentials(cred[0], cred[1])
