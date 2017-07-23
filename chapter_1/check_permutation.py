from collections import Counter


def check_permutation(string_a, string_b):
    return Counter(string_a) == Counter(string_b)
