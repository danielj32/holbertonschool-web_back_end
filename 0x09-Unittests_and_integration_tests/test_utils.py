#!/usr/bin/env python3
""" Parameterize a unit test """
from parameterized import parametized
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json
from utils import memoize
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, result):
        """ test the
        utils.access_nested_map method """
        self.assertEqual(access_nested_map(map, path), result)
