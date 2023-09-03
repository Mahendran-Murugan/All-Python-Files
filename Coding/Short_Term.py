def Short_Term():
    input_str = input()
    list_of_words = input_str.split(" ")
    short_form_str = ""
    for words in list_of_words:
        short_form_str += words[0].upper()
    print(short_form_str)


Short_Term()
Short_Term()
