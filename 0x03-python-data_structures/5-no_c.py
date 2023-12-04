#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for st in my_string:
        if st != 'c' and st != 'C':
            str += st
    return str
