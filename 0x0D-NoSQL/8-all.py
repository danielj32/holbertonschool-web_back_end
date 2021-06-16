#!/usr/bin/env python3
""" List all the
documents in collection """


def list_all(mongo_collection):
    """ function lists
all documents in a collection """
    i = mongo_collection.find()
    return i if i else []
