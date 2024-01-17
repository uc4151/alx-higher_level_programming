#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        str_len = len(sentence)
    else:
        str_len = 0
    return (str_len, sentence if not sentence else sentence[:1])
