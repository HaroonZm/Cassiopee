# valeurs lues en une fois, séparées par des espaces
A, B, C = [int(x) for x in input().split()]
# je suppose qu'il faut qu'ils soient tous pareils ?
if A == B and B == C:
    print("Yes") # on affiche Oui si tout va bien
else:
    print("No")   # sinon Non (dommage)