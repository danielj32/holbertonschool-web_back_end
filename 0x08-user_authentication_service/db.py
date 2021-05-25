#!/usr/bin/env python3
""" Module of DB """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """ Definition of DB class """

    def __init__(self) -> None:
        """ Initialize a new DB instance for the ORM """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ creates a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ saves the user to the database. """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ finds a User taking in kwargs"""
        if not kwargs:
            raise InvalidRequestError

        total = self._session.query(User).filter_by(**kwargs).first()
        if not total:
            raise NoResultFound
        return total
