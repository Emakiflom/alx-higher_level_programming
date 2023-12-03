#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    i = 0
    for a in sys.argv:
        if i > 0:
            suma += int(a)
        i += 1
    print(suma)
