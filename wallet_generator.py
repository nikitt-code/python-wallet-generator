import json
import random


# 370100 words in current database


def load_dictionary(dictionary_name: str) -> dict:
    with open(dictionary_name, "r") as file:
        return json.loads(file.read())


def select_randomly_words(words_count: int = 12) -> dict or bool:
    if words_count == 12 or words_count == 24:

        dictionary: dict = load_dictionary("words_dictionary.json")
        dictionary_list: list = list(dictionary.items())

        selected_dictionary: dict = {}

        for x in range(1, words_count + 1):
            selected_dictionary[x] = random.choice(dictionary_list)[0]

        return selected_dictionary
    else:
        return False


def create_private_key(words_dictionary: dict):
    binary_words_dictionary = []

    for word in words_dictionary:
        current_word = int("".join(format(x, 'b') for x in bytearray(words_dictionary[word], 'utf-8')), 2)
        binary_words_dictionary.append(current_word)

    hash_multiply = binary_words_dictionary[0]
    for x in range(1, len(words_dictionary)):
        hash_multiply *= binary_words_dictionary[x]

    return hex(hash_multiply)
