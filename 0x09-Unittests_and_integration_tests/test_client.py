""" Tests for file clients """
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
from utils import get_json
import unittest


class GithubOrgClient(unittest.TestCase):
    """ class test for For GitHub """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org):
        """ method testing """
        testing = GithubOrgClient(org)
        self.assertEqual(testing.org(),
                         "https://api.github.com/orgs/{}".format(org))
