def print_upper_words(words, must_start_with=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']):
    """Prints out an uppercased version of words in a list"""

    for word in words:
        for letter in must_start_with:
          if word.lower().startswith(letter):
            print(word.upper())