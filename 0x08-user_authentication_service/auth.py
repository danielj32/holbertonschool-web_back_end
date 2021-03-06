#!/usr/bin/env python3
"""
Auth db
"""
from flask.globals import session
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> str:
    """
    salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate a new string
    representation of a new UUID """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            mypass = _hash_password(password)
            user = self._db.add_user(email, mypass)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """  expect email and
        password required arguments and return a boolean """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ takes an email
        string argument
        and returns
        the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """gets a user
        from its session_id """
        if not session_id:
            return None
        try:
            origin = self._db.find_user_by(session_id=session_id)
            return origin
        except NoResultFound:
            None

    def destroy_session(self, user_id: int) -> None:
        """ takes a single user_id
        integer argument and returns None
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ Method that
        reset a password """
        try:
            origin = self._db.find_user_by(email=email)
            tokens = _generate_uuid()
            self._db.update_user(origin.id, reset_token=tokens)
            return tokens
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """  Update password
        for a new password
        """
        try:
            email = self._db.find_user_by(reset_token=reset_token)
            new_pass = _hash_password(password)
            self._db.update_user(email.id, hashed_password=new_pass,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError
