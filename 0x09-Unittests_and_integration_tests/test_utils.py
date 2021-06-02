#!/usr/bin/env python3
""" Test for file utils """
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ tests access_nested_map function """
        self.assertEquals(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ tests access_nested_map's exception """
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    """ get_json
    testing class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, class_mock):
        """ tests get_json function """
        class_mock.return_value = test_payload
        self.assertEquals(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Class to
    the test memoization """
    def test_memoize(self):
        """ memoize method """
        class TestClass:
            """ TestClass to
            test memoization"""
            def a_method(self):
                """ Returns int 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns the method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_f:
            t = TestClass()
            self.assertEqual(t.a_property, mock_f.return_value)
            self.assertEqual(t.a_property, mock_f.return_value)
            mock_f.assert_called_once()
