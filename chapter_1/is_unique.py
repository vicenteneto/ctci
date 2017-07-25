# -*- coding: utf-8 -*-


def is_unique(string, character_set_size=None):
    """
    Time complexity: O(n)
    Space complexity: O(min(c, n))

    Where "n" is the length of the string and "c" is the size of the character set.

    Examples of character set sizes:
        ASCII - 128
        Extended ASCII - 256

    :type string: str, unicode
    :type character_set_size: int
    """

    if character_set_size is not None and len(string) > character_set_size:
        return False

    char_map = {}
    for letter in string:
        if letter in char_map:
            return False
        char_map[letter] = True
    return True


def is_unique_without_data_structure(string):
    """
    Time complexity: O(n²)
    Space complexity: O(1)

    Where "n" is the length of the string.

    :type string: str, unicode
    """

    count = 0
    for i, s1 in enumerate(string):
        for j, s2 in enumerate(string):
            if i != j and s1 == s2:
                count += 1
                if count > 1:
                    return False
    return True


def is_unique_without_data_structure_sorting_string(string):
    """
    Time complexity: O(n log n)
    Space complexity: O(n)

    Where "n" is the length of the string.

    :type string: str, unicode
    """

    sorted_string = sorted(string)
    for i in range(1, len(string)):
        if sorted_string[i - 1] == sorted_string[i]:
            return False
    return True
