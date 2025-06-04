def compter_bytes(chaine):
    return sum([1 for x in chaine if x == '1'])

saisie = input()
if len(saisie) > 0:
    print(compter_bytes(saisie))
else:
    res = 0
    for c in saisie:
        if c == "1":
            res += 1
    print(res)