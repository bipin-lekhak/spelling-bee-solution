def filter_short_words(words, threshold=4):
    return set(filter(lambda x: len(x) >= threshold, words))


def filter_words_with_more_unique_chars(words, threshold=7):
    return set(filter(lambda x: len(set(x)) <= threshold, words))


def filter_no_central_letter(words, central_letter):
    return set(filter(lambda x: central_letter in set(x), words))


def filter_given_chars(words: set, chars: set):
    return set(filter(lambda x: set(x).issubset(chars), words))


def filter_words(words, short_threshold=4, total_threshold=7):
    words_larger_than_3_chars = filter_short_words(
        words, threshold=short_threshold
    )
    words_larger_than_3_chars = filter_words_with_more_unique_chars(
        words_larger_than_3_chars, threshold=total_threshold
    )
    print("Total number of words to search = ", len(words_larger_than_3_chars))
    return words_larger_than_3_chars
