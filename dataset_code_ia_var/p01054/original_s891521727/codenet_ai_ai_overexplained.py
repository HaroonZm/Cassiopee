# Importation du module Counter depuis la bibliothèque collections
# Counter est une sous-classe de dictionnaire conçue spécialement pour compter les objets hashables (par exemple, les lettres d'une chaîne)
from collections import Counter

# Demander à l'utilisateur de saisir un nombre entier
# La fonction input() lit une ligne depuis l'entrée standard (par défaut le clavier)
# int() convertit la chaîne de caractères saisie en nombre entier
n = int(input())

# Lire une deuxième ligne depuis l'entrée standard (correspondant à la première chaîne de lettres à comparer)
# Counter va ensuite créer un dictionnaire où chaque clé est une lettre et chaque valeur est le nombre de fois où cette lettre apparaît
counter1 = Counter(input())

# Lire une troisième ligne depuis l'entrée standard (correspondant à la seconde chaîne de lettres à comparer)
# Counter fait la même opération de comptage pour cette seconde chaîne
counter2 = Counter(input())

# Maintenant, pour pouvoir comparer les quantités de chaque lettre indépendamment de leur présence/absence dans chaque mot :
# On crée une liste qui contiendra les quantités pour chacune des 26 lettres de l'alphabet anglais ('a' à 'z')
# len(counter1) donne le nombre de lettres différentes présentes dans la première chaîne
# (26 - len(counter1)) donne le nombre de lettres de l'alphabet qui sont absentes de la chaîne
# On crée une liste de zéros de cette longueur, qu'on concatène avec la liste ordonnée des valeurs du Counter
# sorted(counter1.values()) trie dans l'ordre croissant le nombre d'occurrences de chaque lettre présente
# La somme permet d'obtenir une liste de 26 éléments où chaque élément donne la quantité de la lettre correspondante ou 0 si elle était absente
values1 = [0] * (26 - len(counter1)) + sorted(counter1.values())

# Même opération pour le second mot/Counter
values2 = [0] * (26 - len(counter2)) + sorted(counter2.values())

# On veut maintenant calculer la différence absolue du nombre d'occurrences de chaque lettre entre les deux mots
# zip(values1, values2) permet d'itérer en parallèle sur les deux listes de quantités, lettre par lettre (ordre croissant des fréquences)
# Pour chaque couple de quantités, on calcule la valeur absolue de leur différence avec abs(i - j)
# On crée une liste de ces différences
# sum() additionne tous ces écarts absolus
# Le résultat est divisé par 2 en utilisant l'opérateur de division entière '//' :
# Ceci car chaque suppression/insertion d'une lettre "compte double" dans la somme des différences absolues (une lettre en trop dans l'un et en manque dans l'autre)
# Enfin, on affiche le résultat avec la fonction print()
print(sum([abs(i - j) for i, j in zip(values1, values2)]) // 2)