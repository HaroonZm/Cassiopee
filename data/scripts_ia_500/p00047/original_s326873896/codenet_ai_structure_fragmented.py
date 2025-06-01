def lire_entree():
    return input()

def splitter_chaine(chaine):
    return chaine.split(',')

def remplacer_now(now, a, b):
    if now == a:
        return b
    elif now == b:
        return a
    else:
        return now

def boucle_principale():
    now = 'A'
    while True:
        try:
            entree = lire_entree()
            a, b = splitter_chaine(entree)
            now = remplacer_now(now, a, b)
        except:
            break
    return now

def main():
    resultat = boucle_principale()
    print(resultat)

main()