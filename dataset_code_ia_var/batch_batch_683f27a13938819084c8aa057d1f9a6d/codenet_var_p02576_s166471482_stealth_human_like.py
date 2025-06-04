# Bon, alors on prend les valeurs (je suppose qu'on les donne à l'entrée ?)
n, x, t = map(int, input().split())  # pas besoin de list ici je crois, mais bon

# Ca c'est pour compter les "cycles"
resultat = (n // x) * t

# Parfois il reste un peu plus... dans ce cas faut rajouter un tour pour ceux qui restent
reste = n % x
if reste != 0:
    resultat = resultat + t  # rajout, mais je me demande si on pouvait faire autrement

# Affichage final, on verra si ça donne ce qu'on veut
print(resultat)