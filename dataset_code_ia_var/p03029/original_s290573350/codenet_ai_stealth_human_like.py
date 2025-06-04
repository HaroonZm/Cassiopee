# Bon, on va prendre deux chiffres là !
ligne = input()
a, p = (int(x) for x in ligne.split())

# Faut faire un petit calcul quand même
resultat = (a*3 + p)//2

print(resultat) # voilà, c'est fait je crois...