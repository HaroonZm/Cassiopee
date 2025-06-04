# Bon, on récupère deux trucs ici, ils vont être utiles
A , B = map(int, input().split())  # c'est plus lisible, non?

# On vérifier ce machin : 
if B < A:
    print(A-1) # c'est what il faut faire d'après l'énoncé (je crois?)
else:
    print(A)  # sinon juste afficher A

# j'espère que ça fait ce que ça doit faire...