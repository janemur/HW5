from typing import List, Tuple
import urllib.request
import unittest
from unittest.mock import patch
import io
from ohe import what_is_year_now


class TestYear(unittest.TestCase):
    def test_first_format(self):
        mini_api = '{"currentDateTime": "2019-03-01"}'

        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(mini_api)):
            actual = what_is_year_now()
        expected = 2019
        self.assertEqual(actual, expected)

    def test_second_format(self):
        mini_api = '{"currentDateTime": "01.03.2019"}'

        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(mini_api)):
            actual = what_is_year_now()
        expected = 2019
        self.assertEqual(actual, expected)

    def test_exception(self):
        mini_api = '{"currentDateTime": "01/03/2019"}'

        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(mini_api)):
            with self.assertRaises(ValueError):
                what_is_year_now()



