import pytest
from .numberChecking import *


def test_odd_or_even():
    given = 3
    expected = "odd"
    got = odd_or_even(given)
    assert got == expected


def test_is_odd():
    given = [0, 2, 3, 4]
    expected = [False, False, True, False]
    for i in range(len(given)):
        got = is_odd(given[i])
        assert got == expected[i]
        # assert is_odd(given[i]) == expected[i] # not a good practice


def test_is_even():
    given = [0, 2, 3, 4]
    expected = [True, True, False, True]
    for i in range(len(given)):
        got = is_even(given[i])
        assert got == expected[i]
        # assert is_odd(given[i]) == expected[i] # not a good practice


def test_is_digit():
    given = ["0", "a", "b", "1", "2", "c", "."]
    expected = [True, False, False, True, True, False, False]
    for i in range(len(given)):
        got = is_digit(given[i])
        assert got == expected[i]


def test_is_integer_for_valid_number():
    given = ["00000", "1234", "000135", "0123456789"]
    expected = [True, True, True, True]
    for i in range(len(given)):
        got = is_integer(given[i])
        assert got == expected[i]


def test_is_integer_for_invalid_number():
    # given = ["0.1", "0b111", "mm", ""]
    # expected = [False, False, False, False]
    tests = [
        {"given": "0.1", "expected": False},
        {"given": "0b111", "expected": False},
        {"given": "0xA0", "expected": False},
        {"given": "0c36", "expected": False},
        {"given": "KK", "expected": False},
        {"given": "", "expected": False},
    ]

    for test in tests:
        got = is_integer(test["given"])
        assert got == test["expected"], \
            'given: "{}", expected: "{}", got: "{}"'.format(test["given"], test["expected"], got)


def test_odd_or_even_str_to_int():
    tests = [
        {"given": "3", "expected": "odd"},
        {"given": "100", "expected": "even"},
        {"given": "29", "expected": "odd"},
        {"given": "88", "expected": "even"},
    ]

    for test in tests:
        got = odd_or_even_str_to_int_conversion(test["given"])
        assert got == test["expected"], \
            'given: "{}", expected: "{}", got: "{}"'.format(test["given"], test["expected"], got)


def test_odd_or_even_str_to_int_invalid_number():
    given = "abc"
    expected = "Invalid Number"
    with pytest.raises(ValueError, match=expected):
        odd_or_even_str_to_int_conversion_2(given)

