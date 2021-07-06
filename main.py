from wallet_generator import *

if __name__ == '__main__':

    type_check: str = input("Enter check_type (1 - create / 2 - validate): ")

    if type_check == "create" or type_check == "1":
        words: dict = select_randomly_words(12)
        private_key: str = create_private_key(words)

        # for validate
        words_string: str = ";"
        for x in words: words_string += ";" + words[x]
        words_string = words_string.replace(";;", "")

        print("Words: ", words)
        print("Words string: ", words_string)
        print("Private key: ", private_key)

    elif type_check == "validate" or type_check == "2":
        in_words: str = input("Enter secret words (string - word1;word2;..;word12: ")
        in_private_key: str = input("Enter private key: ")

        words_pre_dict = in_words.split(';')
        words_dictionary = {}
        for x in range(len(words_pre_dict)):
            words_dictionary[(x + 1)] = words_pre_dict[x]

        private_key: str = create_private_key(words_dictionary)

        if private_key == in_private_key:
            print("All is valid")
        else:
            print("Something is wrong")
