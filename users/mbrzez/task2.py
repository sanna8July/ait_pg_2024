checked_word = "settesttse"
list_of_words = ['set', 'test', 'tse']


def check_if_contains(word: str, words: list) -> bool:
    word_temp = word

    for word_el in words:
        if word_el in word_temp:
            word_temp = word_temp.replace(word_el, '')

            if word_temp == '':
                return True

    return False


if __name__ == "__main__":
    print(check_if_contains(checked_word, list_of_words))


