"""
import math

values = {}
values.update(divide(num[0]))
i = 1
while i < len(num):
    values.update(divide(num[:i]))
    unique = set(values.values())
    for val in unique:
        if values.values().count(val) > 1:
            return False
    i += 1


def divide(num):
    if len(num)-1 == 0:
        return {num:num}
    i = 0
    lgt = len(num)
    values = {}
    while i < lgt:
        values[num[i+1:]] = math.prod([int(x) for digit in num[i+1:]])
        i += 1
    return values
"""
import numpy

def colorful_number(num):
    if '0' in num or '1' in num:
        return False
    if len(set(num)) != len(num):
        return False
    values = dict(zip([x for x in num], [int(x) for x in num]))
    i = 1
    while i < len(num):
        values.update(divide(num[:i+1]))
        if num in values:
            del values[num]
        unique = set(values.values())
        for val in unique:
            if list(values.values()).count(val) > 1:
                return False
        i += 1
    return True

def divide(num):
    i = 0
    lgt = len(num)
    values = {}
    while i < lgt-1:
        values[num[i:]] = int(numpy.prod([int(digit) for digit in num[i:]]))
        i += 1
    return values


# print(colorful_number('326'))
# print(colorful_number('3245'))
# print(colorful_number('54321'))
# print(colorful_number('357'))
# print(colorful_number('359682'))
# print(colorful_number('23456789'))
print(colorful_number('23456789'))
