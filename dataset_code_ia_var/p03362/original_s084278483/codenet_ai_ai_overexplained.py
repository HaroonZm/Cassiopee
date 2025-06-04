# Importer toutes les fonctions du module math pour utiliser des fonctions mathématiques de base
from math import *

# Lire une valeur saisie par l'utilisateur, la convertir en entier, et l'affecter à la variable n
# input() retourne une chaîne de caractères ; int() convertit cette chaîne en entier
n = int(input())

# Créer un ensemble (set) de tous les entiers de 2 jusqu'à (et y compris) 55555
# range(2, 55556) génère une séquence de nombres de 2 à 55555
# set() construit un ensemble à partir de cette séquence
ps = set(range(2, 55556))

# Commencer une boucle pour parcourir tous les entiers i de 2 jusqu'à la racine carrée de 55555, arrondie à l'entier inférieur, puis en ajouter 1
# Ceci est nécessaire pour appliquer efficacement le crible d'Ératosthène
for i in range(2, floor(sqrt(55555) + 1)):
    # Vérifier si le nombre courant i est encore présent dans l'ensemble ps (c'est-à-dire qu'il est considéré premier)
    if i in ps:
        # Initialiser un multiplicateur k à 2 pour générer les multiples de i
        k = 2
        # Boucle pour marquer comme composés tous les multiples de i qui sont inférieurs ou égaux à 55555
        # i*k représente un multiple de i
        while(i * k <= 55555):
            # Vérifier si le multiple courant fait encore partie de l'ensemble ps
            if i * k in ps:
                # Supprimer ce nombre de l'ensemble car il n'est pas premier (c'est un multiple d'un nombre premier)
                ps.remove(i * k)
            # Passer au prochain multiple
            k += 1

# Initialiser une liste vide pour stocker les réponses ou les résultats finaux
ans = []

# Déterminer le plus grand nombre premier dans l'ensemble ps avec max(ps), et assigner cette valeur à la variable i
i = max(ps)

# Démarrer une boucle qui continue tant que la longueur de la liste ans est strictement inférieure à n ET que i est inférieur ou égal à 55555
while len(ans) < n and i <= 55555:
    # Vérifier si le nombre courant i se trouve dans l'ensemble ps, c'est-à-dire s'il s'agit d'un nombre premier
    if i in ps:
        # Ajouter ce nombre à la liste ans, ce qui signifie que ce nombre premier fait partie des résultats
        ans.append(i)
    # Décrémenter la valeur de i de 25, pour passer au nombre précédent à examiner
    i -= 25

# Afficher le contenu de la liste ans sous forme d'une séquence d'entiers séparés par des espaces
# L'opérateur * décompresse la liste ans afin que chaque élément soit passé comme argument séparé à print()
print(*ans)