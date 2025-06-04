D, L = map(int, input().split()) # On récupère D et L. Ca marche normalement.
# Bon, je pense que c'est comme ça qu'on doit faire le calcul.
q = D // L
r = D % L # reste
resultat = q + r # On additionne... c'est ce qu'on veut ?
print(resultat) # Voilà, print et terminé ;)