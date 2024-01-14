def print_upper_words(words):
    """Prints out an uppercased version of words in a list"""

    for word in words:
        if word.lower().startswith('e'):
          print(word.upper())