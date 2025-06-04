# Bon, voilà mon essai, j'espère que c'est clair...
mot = input() # On récupère la chaîne utilisateur

A = 0
nb_k = mot.count("K")
nb_u = mot.count("U")
nb_p = mot.count("P")
nb_c = mot.count("C")

# Je pense que c'est comme une sorte de boucle pour enlever chaque lettre
while 1:
    if nb_k==0 or nb_u==0 or nb_p==0 or nb_c==0:
        # si une lettre manque, on sort
        break
    else:
        A = A + 1
        nb_k = nb_k - 1
        nb_u -= 1 # ça marche comme ça aussi normalement
        nb_p = nb_p - 1
        nb_c = nb_c - 1 # il ne faut pas oublier C, non ?

print(A)  # Voilà le résultat, c'est ça non?