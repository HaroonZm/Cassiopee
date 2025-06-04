# Bon, on va demander à l'utilisateur un nombre
x = input("Entrez un nombre, svp : ")
# ptet que ça rentre pas un int, mais on va essayer
try:
    x = int(x)
except:
    print("Vous devez écrire un nombre entier !!")
    x = 0  # hmm, pas sûr mais bon

# On fait le calcul bizarre demandé
resu = x + (x*x) + x**3
print("Le résultat final est :",resu)
# Voilà, c'est fait...