def lire_ensembles(n):
    return [set(map(int, input().split())) for _ in range(n)]

def compter_occurrences(lst, x):
    return lst.count(x)

def extraire_paires(lst):
    rec = []
    while lst:
        x = lst[0]
        count = compter_occurrences(lst, x)
        if count % 2 == 1:
            return None
        rec.append((count, x))
        for _ in range(count):
            lst.pop(lst.index(x))
    return rec

def verifier_une_paire(rec):
    if len(rec[0][1]) == 1:
        return True
    return False

def verifier_deux_paires(rec):
    rec.sort()
    if rec[0][1] & rec[1][1] == rec[0][1]:
        return True
    return False

def verifier_trois_paires(rec):
    a, b, c = rec[0][1], rec[1][1], rec[2][1]
    if len(a) == len(b) == len(c) == 2 and (c & (a | b) == c):
        return True
    return False

def afficher_resultat(rec):
    if len(rec) == 1:
        if verifier_une_paire(rec):
            print("yes")
        else:
            print("no")
    elif len(rec) == 2:
        if verifier_deux_paires(rec):
            print("yes")
        else:
            print("no")
    elif len(rec) == 3:
        if verifier_trois_paires(rec):
            print("yes")
        else:
            print("no")
    else:
        print("no")

def main():
    lst = lire_ensembles(6)
    rec = extraire_paires(lst)
    if rec is None:
        print("no")
    else:
        afficher_resultat(rec)

main()