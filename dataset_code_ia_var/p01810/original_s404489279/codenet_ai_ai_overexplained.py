# Demande à l'utilisateur de saisir deux entiers séparés par des espaces.
# La fonction input() lit une ligne de texte depuis le clavier.
# La méthode split() sépare cette ligne en une liste de chaînes en utilisant les espaces comme séparateurs.
# La fonction map() applique la fonction int à chaque élément de la liste, ce qui convertit chaque chaîne de caractères en entier.
# Enfin, les deux entiers résultants sont affectés respectivement aux variables n et k.
n, k = map(int, input().split())

# Initialise la variable 'now' à 0.
# Cette variable servira à stocker le résultat intermédiaire durant la boucle while suivante.
now = 0

# Démarre une boucle while qui se poursuit tant que la variable n est strictement supérieure à 1.
# Cela signifie que la boucle s'exécutera tant que la condition n > 1 est vraie.
while n > 1:
    # Décrémente la variable n de 1 à chaque itération de la boucle.
    # Cela revient à remplacer n par n - 1.
    n -= 1
    # Met à jour la valeur de 'now' à l'aide d'une formule mathématique.
    # À chaque étape, on multiplie la valeur actuelle de 'now' par k,
    # puis on divise le produit par (k - 1) en utilisant la division entière //
    # qui retourne la partie entière du résultat (c'est-à-dire qu'elle arrondit à l'entier inférieur en cas de résultat décimal).
    # Ensuite, on ajoute 1 au résultat obtenu.
    now = (now * k) // (k - 1) + 1

# Affiche la valeur finale de 'now' sur la sortie standard (c'est-à-dire à l'écran).
# La fonction print() affiche son argument à l'écran suivi d'un saut de ligne par défaut.
print(now)