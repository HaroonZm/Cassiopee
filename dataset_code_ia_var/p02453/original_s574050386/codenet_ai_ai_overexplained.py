from bisect import bisect  # Importe la fonction bisect du module bisect, qui permet d'effectuer des recherches efficaces dans des listes triées

# Assigne à la variable readline la méthode readline de l'objet fichier ouvert correspondant à l'entrée standard (descripteur 0)
# Cela permet de lire les lignes de l'entrée standard rapidement
readline = open(0).readline

# Lit une ligne depuis l'entrée standard (l'utilisateur, ou un fichier si redirigé)
# La fonction readline() retourne une chaîne de caractères contenant la ligne lue, y compris le caractère de fin de ligne '\n'
# int() convertit cette chaîne en un entier
N = int(readline())

# Lit une autre ligne de l'entrée standard contenant N entiers séparés par des espaces
# readline() lit la ligne, split() divise la chaîne en sous-chaînes selon les espaces
# map(int, ...) transforme chaque sous-chaîne en entier
# *A, = (...) permet de stocker la séquence d'entiers résultante dans une liste appelée A, grâce à l'unpacking
*A, = map(int, readline().split())

# Ouvre la sortie standard (descripteur 1, typiquement l'écran ou la redirection de sortie) en mode écriture ('w')
# La méthode writelines() permet d'écrire de multiples chaînes de caractères dans le fichier de sortie
# [...] construit une liste des chaînes à écrire, chacune contenant le résultat d'une recherche bisect pour une requête donnée

open(1, 'w').writelines(
    [   # La liste suivante s'insère comme argument unique de writelines
        "%d\n" % bisect(           # "%d\n" permet de formater un entier suivi d'un retour à la ligne
            A,                     # On recherche dans la liste triée A
            int(readline()) - 1    # On lit un entier de l'entrée, on le convertit, puis on soustrait 1 (décalage d'indice)
        )
        for q in range(            # On construit cette liste pour chaque requête, le nombre de requêtes est donné par...
            int(readline())        # ...l'entier lu à la ligne suivante
        )
    ]
)
# Au final, pour chaque requête, on insère dans la liste les résultats de bisect() dans A à la position (requête-1),
# on formate ce résultat comme une chaîne avec retour à la ligne, et on les écrit toutes à la sortie standard