checked_word = "settesttse"
list_of_words = ['set', 'test', 'tse']


def check_if_contains(word: str, words: list) -> bool:
    temp_word = word

    while len(temp_word) > 0:
        for word_to_remove in words:
            if word_to_remove in temp_word:
                temp_word = temp_word.replace(word_to_remove, '')

    return True


if __name__ == "__main__":
    print(check_if_contains(checked_word, list_of_words))
