from string_utils import StringUtils


def test_capitalize():
    str_util = StringUtils()
    assert str_util.capitalize("hello") == "Hello"
    assert str_util.capitalize("WORLD") == "World"
    assert str_util.capitalize("123") == "123"


def test_trim():
    str_util = StringUtils()
    assert str_util.trim("  hello") == "hello"
    assert str_util.trim("   world") == "world"
    assert str_util.trim(" 123") == "123"


def test_to_list():
    str_util = StringUtils()
    assert str_util.to_list("hello,world") == ["hello", "world"]
    assert str_util.to_list("1,2,3") == ["1", "2", "3"]
    assert str_util.to_list("apple") == ["apple"]


def test_contains():
    str_util = StringUtils()
    assert str_util.contains("hello world", "ll") == True
    assert str_util.contains("12345", "6") == False
    assert str_util.contains("abcabc", "b") == True


def test_delete_symbol():
    str_util = StringUtils()
    assert str_util.delete_symbol("hello world", "o") == "hell wrld"
    assert str_util.delete_symbol("abcabcabc", "c") == "ababab"
    assert str_util.delete_symbol("12345", "6") == "12345"


def test_starts_with():
    str_util = StringUtils()
    assert str_util.starts_with("hello world", "he") == True
    assert str_util.starts_with("12345", "2") == False
    assert str_util.starts_with("apple", "ap") == True


def test_end_with():
    str_util = StringUtils()
    assert str_util.end_with("hello world", "ld") == True
    assert str_util.end_with("12345", "2") == False
    assert str_util.end_with("apple", "le") == True


def test_is_empty():
    str_util = StringUtils()
    assert str_util.is_empty("") == True
    assert str_util.is_empty("hello") == False
    assert str_util.is_empty("  ") == True


def test_list_to_string():
    str_util = StringUtils()
    assert str_util.list_to_string(["apple", "banana", "cherry"]) == "apple, banana, cherry"
    assert str_util.list_to_string(["1", "2", "3"], "-") == "1-2-3"
    assert str_util.list_to_string(["hello world"]) == "hello world"
