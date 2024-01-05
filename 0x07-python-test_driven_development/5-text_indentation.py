#!/usr/bin/python3
# text_indentation module
def text_indentation(text=None):
    # text_indentation
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    text1 = ""
    char_list = ['.', '?', ':']
    text1 = text.strip(" ")

    for i in range(len(text1)):
        if (text1[i] in char_list):
            print(text1[i], end="\n\n")
        elif (text1[i] != " " and (text1[i - 1] != " ") or
              text1[i - 1] not in char_list):
            print(text1[i], end="")
