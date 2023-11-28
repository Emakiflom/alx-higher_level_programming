#!/usr/bin/python3
charend = ", "
for i in range(0, 100):
    digit2 = i % 10
    digit1 = i / 10
    if i < 10 and digit1 < digit2:
        print("{}{}".format(0, i), end=charend)
    elif digit1 < digit2:
        if i == 89:
            charend = "\n"
        print(i, end=charend)
