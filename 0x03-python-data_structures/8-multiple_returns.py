#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        list = [len(sentence), None]
        new_tuplex = tuple(list)
    else:
        list = [len(sentence), sentence[0]]
        new_tuplex = tuple(list)
    return new_tuplex
