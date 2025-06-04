import itertools as i  # Importe le module itertools et lui donne l'alias 'i' pour un accès plus rapide
import collections as c  # Importe le module collections avec l'alias 'c' pour raccourcir l'écriture

# Lis toutes les lignes de l'entrée standard, puis les divise en mots (espaces/blancs sont séparateurs)
# le résultat est une liste de chaînes de caractères. La première correspond à 'n' (nombre d'éléments),
# les suivantes constituent 'a' (la liste des chaînes à traiter).
n, *a = open(0).read().split()

# On va compter le nombre d'occurrences pour chaque première lettre des mots de 'a',
# mais uniquement si la première lettre fait partie de 'M', 'A', 'R', 'C', 'H'
filtered_first_letters = [s[0] for s in a if s[0] in "MARCH"]  # Pour chaque mot 's', on prend s[0] si c'est une des lettres recherchées

# Utilise Counter pour compter, pour chaque première lettre, combien de mots commencent par cette lettre
letter_counts = c.Counter(filtered_first_letters)  # Crée un dictionnaire : lettre -> occurrence

# Prend les valeurs du compteur, c'est-à-dire, le nombre d'éléments pour chacune des lettres sélectionnées
count_values = letter_counts.values()  # Liste du style [2, 5, 0, 3, 1] (chaque élément : nb de mots pour une lettre de 'MARCH')

# Calcule tous les triplets possibles de trois différentes lettres parmi celles trouvées (combinaisons sans répétition)
combinations_of_counts = i.combinations(count_values, 3)  # Génère un itérable de triplets : (compte1, compte2, compte3)

# Pour chaque combinaison triplet (p, q, r), calcule leur produit p * q * r (nombre de façons de choisir un mot pour chaque lettre)
products = (p * q * r for (p, q, r) in combinations_of_counts)  # Génère une séquence de ces produits

# Additionne l'ensemble de ces produits pour obtenir le résultat final, qui est le nombre total de combinaisons possibles
total = sum(products)

# Affiche ce résultat sur la sortie standard
print(total)