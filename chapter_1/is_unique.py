def is_unique(string):
    unique_chars = set(string)
    return len(string) == len(unique_chars)


def is_unique_without_data_structure(string):
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
