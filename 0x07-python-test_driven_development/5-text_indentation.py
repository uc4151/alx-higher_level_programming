#!/usr/bin/python3
""" Defines a text indentation function """


def text_indentation(text):
    """Print a text with two lines after writing >, ? and : chars

    Args:
        text(str): the text to be printed
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1 
