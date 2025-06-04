cou = 0
mot = input().lower()

while True:
    ligne = input()
    mots = ligne.split()
    if len(mots) > 0 and mots[0] == "END_OF_TEXT":
        break
    for m in mots:
        if m.lower() == mot:
            cou = cou + 1

print(cou)