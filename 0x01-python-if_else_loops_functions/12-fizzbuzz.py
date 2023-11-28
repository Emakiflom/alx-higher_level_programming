#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz", end=" ")
        elif (i % 5) == 0:
            print("Buzz", end=" ")
        elif (i % 3) == 0:
            print("Fizz", end=" ")
        else:
            if i != 99:
                print(i, end=" ")
            else:
                print(i, end="")
