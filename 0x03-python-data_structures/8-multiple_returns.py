#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        t = length, None
    else:
        t = length, sentence[0]
    return t
