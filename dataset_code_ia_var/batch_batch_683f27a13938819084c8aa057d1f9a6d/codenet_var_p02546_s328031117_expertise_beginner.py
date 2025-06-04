mot = input()

if mot[len(mot) - 1] == "s":
    print(mot + "es")
else:
    print(mot + "s")