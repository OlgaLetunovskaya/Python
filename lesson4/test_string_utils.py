import unittest
from string_utils import StringUtils
string_utils = StringUtils()

class StringUtilsTests(unittest.TestCase):

    def setUp(self):
        self.utils = StringUtils()

    def test_capitalize_positive(self):
        result = self.utils.capitalize("hello")
        self.assertEqual(result, "Hello")

    def test_capitalize_negative(self):
        result = self.utils.capitalize("WORLD")
        self.assertNotEqual(result, "WORLD")

def test_trim_positive(self):
    result = self.utils.trim("  hello  ")
    self.assertEqual(result, "hello")

def test_trim_negative(self):
    result = self.utils.trim("  hello  ")
    self.assertNotEqual(result, "  hello")

def test_to_list_positive(self):
    result = self.utils.to_list("apple,banana,orange")
    self.assertEqual(result, ["apple", "banana", "orange"])

def test_to_list_negative(self):
    result = self.utils.to_list("apple,banana,orange")
    self.assertNotEqual(result, ["apple", "banana"])

def test_contains_positive(self):
    result = self.utils.contains("hello world", "o")
    self.assertTrue(result)

def test_contains_negative(self):
    result = self.utils.contains("hello world", "x")
    self.assertFalse(result)

def test_delete_symbol_positive(self):
    result = self.utils.delete_symbol("hello world", "o")
    self.assertEqual(result, "hell wrld")

def test_delete_symbol_negative(self):
    result = self.utils.delete_symbol("hello world", "o")
    self.assertNotEqual(result, "hello world")

def test_starts_with_positive(self):
    result = self.utils.starts_with("hello world", "h")
    self.assertTrue(result)

def test_starts_with_negative(self):
    result = self.utils.starts_with("hello world", "x")
    self.assertFalse(result)

def test_end_with_positive(self):
    result = self.utils.end_with("hello world", "d")
    self.assertTrue(result)

def test_end_with_negative(self):
    result = self.utils.end_with("hello world", "x")
    self.assertFalse(result)

def test_is_empty_positive(self):
    result = self.utils.is_empty("")
    self.assertTrue(result)

def test_is_empty_negative(self):
    result = self.utils.is_empty("hello")
    self.assertFalse(result)

def test_list_to_string_positive(self):
    result = self.utils.list_to_string(["apple", "banana", "orange"])
    self.assertEqual(result, "apple, banana, orange")

def test_list_to_string_negative(self):
    result = self.utils.list_to_string(["apple", "banana", "orange"])
    self.assertNotEqual(result, "apple, banana")

