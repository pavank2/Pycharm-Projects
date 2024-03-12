import pytest

from removeDuplicates import remove_duplicates

def test_array_with_same_values():
    input = [2,2,2,2,2]
    expected = [2]

    assert remove_duplicates(input) == expected