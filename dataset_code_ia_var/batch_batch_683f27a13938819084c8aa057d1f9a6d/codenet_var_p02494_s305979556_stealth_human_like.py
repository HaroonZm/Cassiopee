#!/usr/bin/python
# ok, on va réécrire ça "à ma sauce"

while True:
    # input, je suppose qu'on attend deux entiers ?
    line = raw_input()
    vals = line.split()
    a = int(vals[0])
    b = int(vals[1])
    if a == 0 and b == 0:
        break
    for i in range(a):
        print("#" * b)
    print   # un print vide pour sauter une ligne... (est-ce que ça marche encore en Python3 d'ailleurs?)