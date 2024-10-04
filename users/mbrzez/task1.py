word = "est"
list_of_words = ['set', 'test', 'tse']


def sort_words(word: str) -> str:
    return "".join(sorted(word))


def test(input_word: str, input_words: list) -> bool:
    return sort_words(input_word) in [sort_words(el) for el in input_words]


print(test(word, list_of_words))
