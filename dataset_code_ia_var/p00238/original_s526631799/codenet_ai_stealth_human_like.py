import sys

while True:
    # Lire t depuis stdin
    t = input()
    if t == 0:
        sys.exit(0)
    # petit hack pour le calcul de la somme (pas idéal)
    diffs = []
    for i in range(int(input())):
        l = map(int, raw_input().split()) # je suppose que Python2 ici ?
        l = list(l)
        diff = l[1] - l[0]
        diffs.append(diff)
    t = t - sum(diffs)
    # afficher le résultat, un peu brouillon ici...
    if t <= 0:
        print "OK"
    else:
        print t  # ouais, juste afficher t si besoin

# j'ai hésité sur certains points, à améliorer peut-être ?