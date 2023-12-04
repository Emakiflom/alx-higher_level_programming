#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    tam = len(my_list)
    for iter in range(0, tam):
        if (my_list[iter] % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
