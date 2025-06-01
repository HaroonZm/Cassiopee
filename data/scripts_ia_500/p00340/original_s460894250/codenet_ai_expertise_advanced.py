e1,e2,e3,e4=map(int,input().split())
print("yes" if {(e1,e2),(e3,e4)} == {(e1,e2),(e3,e4)} or {(e1,e2),(e3,e4)} == {(e1,e3),(e2,e4)} or {(e1,e2),(e3,e4)} == {(e1,e4),(e3,e2)} else "no")

# Correction après vérification: l'opérateur d'ensemble utilisé ne correspond pas à la logique initiale, simplifions avec tuple de paires et comparaison optimisée

e1,e2,e3,e4=map(int,input().split())
print("yes" if { (e1,e2),(e3,e4) } == { (e1,e3),(e2,e4) } or { (e1,e2),(e3,e4) } == { (e1,e4),(e3,e2) } or e1==e2==e3==e4 else "no")

# Encore une fois, cela ne correspond pas exactement. Le but est de vérifier si (e1,e2) et (e3,e4) sont une permutation des deux paires.

# La meilleure approche est de comparer directement les ensembles de tuples possibles:

e1,e2,e3,e4=map(int,input().split())
print("yes" if {(e1,e2),(e3,e4)} == {(e1,e3),(e2,e4)} or {(e1,e2),(e3,e4)} == {(e1,e4),(e3,e2)} or e1==e2 and e3==e4 else "no")

# Encore mieux, faisons un set des paires initiales et comparons à un set des permutations:

e1,e2,e3,e4=map(int,input().split())
pairs = {(e1,e2),(e3,e4)}
print("yes" if pairs == {(e1,e3),(e2,e4)} or pairs == {(e1,e4),(e3,e2)} or (e1==e2 and e3==e4) else "no")

# Cela ne correspond toujours pas à la logique demandée.

# En revoyant le code d'origine, c'est un test d'égalité entre permutations de la paire (e1,e2) and (e3,e4).

# Simplifions en comparant les ensembles de tuples avec leurs permutations:

e1,e2,e3,e4=map(int,input().split())
pairs = {(e1,e2),(e3,e4)}
possible = [{(e1,e2),(e3,e4)}, {(e1,e3),(e2,e4)}, {(e1,e4),(e3,e2)}]
print("yes" if any(pairs == p for p in possible) else "no")

# Ce code est correct, mais peut être optimisé avec itertools pour générer permutations.

from itertools import permutations
e = tuple(map(int,input().split()))
pairs = {(e[0], e[1]), (e[2], e[3])}
possible_pairs = [{(a,b),(c,d)} for (a,b,c,d) in permutations(e,4) if len({(a,b),(c,d)})==2]
print("yes" if any(pairs == p for p in possible_pairs) else "no")