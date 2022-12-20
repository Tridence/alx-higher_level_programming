#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    result = 0

    for in in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")

            result += a ** b / i
        except:
            result = b + a
            break

    return result
