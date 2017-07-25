def check_permutation(s1, s2):
    """
    Time complexity: O((m + n) log (m * n))
    Space complexity: O(m + n)

    Where "m" is the length of s1 and "n" is the length of s2.

    :type s1: str, unicode
    :type s2: str, unicode
    """

    return len(s1) == len(s2) and sorted(s1) == sorted(s2)


def check_permutation_without_sorting_string(s1, s2):
    """
    Time complexity: O(m + n)
    Space complexity: O(m)

    Where "m" is the length of s1 and "n" is the length of s2.

    :type s1: str, unicode
    :type s2: str, unicode
    """

    if len(s1) != len(s2):
        return False

    char_map = {}
    for letter in s1:
        char_map[letter] = char_map.get(letter, 0) + 1

    for letter in s2:
        char_map[letter] -= 1
        if char_map[letter] < 0:
            return False
    return True
