#!/usr/bin/python3

def multiple_returns(sentence):
    count = 0
    if sentence != '':
        firstChar = sentence[0]
        for i in range(len(sentence)):
            count += 1
    else:
        firstChar = None
    return (count, firstChar)
