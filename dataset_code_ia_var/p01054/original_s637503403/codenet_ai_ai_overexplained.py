# Début du script

# AOJ 1568: String Conversion
# Version avec commentaires extrêmement détaillés

# La fonction ord('a') retourne le code ASCII/unicode correspondant à la lettre 'a'.
# Ici, on l'utilise pour repérer la position de 'a' dans la table ASCII.
cha = ord('a')  # Code ASCII pour 'a' (97)
chzn = ord('z') + 1  # Code ASCII pour 'z' (122) + 1 = 123 (utilisé pour les intervalles fermés ouverts)

# On crée deux listes de taille 128, initialisées à zéro.
# Ces listes serviront de tables de comptage pour chaque code ASCII jusqu'à 127 (inclus).
# La raison de la taille 128 est de couvrir tous les caractères ASCII standards.
S = [0] * 128  # Liste pour compter les lettres de la première chaîne (compteur de fréquence des lettres pour la 1ère string)
T = [0] * 128  # Liste pour compter les lettres de la seconde chaîne (compteur de fréquence des lettres pour la 2ème string)

input()  # On lit la première ligne d'entrée mais elle n'est pas utilisée (souvent il s'agit de la longueur de la string en problème IOI/AOJ)

a = input()  # On lit la première string depuis l'entrée standard.
# À chaque itération, x prendra la valeur d'un caractère de la string.
for x in a:
    # ord(x) donne le code ASCII du caractère x.
    # On incrémente de 1 à l'indice correspondant dans la liste S.
    # Cela permet de compter le nombre d'occurrences de chaque caractère dans la string.
    S[ord(x)] += 1

# On extrait les éléments de la liste S correspondant aux positions des lettres minuscules anglaises (de 'a' à 'z')
# S[cha:chzn] extrait les comptes pour les lettres 'a' à 'z'
# sorted(..., reverse=True) trie la liste extraite en ordre décroissant (de la lettre la plus fréquente à la moins fréquente)
S = sorted(S[cha:chzn], reverse=True)

a = input()  # On lit la seconde chaîne de caractères.
for x in a:
    T[ord(x)] += 1  # Même principe de comptage que plus haut, mais pour la deuxième string

T = sorted(T[cha:chzn], reverse=True)  # On trie aussi la distribution de fréquence de la deuxième chaîne en ordre décroissant

ans = 0  # On initialise le compteur de la somme des différences absolues à zéro

# On fait une boucle pour chacune des 26 lettres de l'alphabet anglais (de 'a' à 'z', donc 26 lettres)
# range(26) génère les entiers de 0 à 25, inclus.
for i in range(26):
    # On calcule la différence absolue entre la fréquence de la lettre i la plus fréquente de la première string et celle de la seconde string
    # abs(...) retourne la valeur absolue de la différence, c'est-à-dire sans signe (toujours positif).
    ans += abs(S[i] - T[i])  # On ajoute cette différence au total

# Enfin, on affiche le résultat.
# L'opérateur >> 1 signifie un 'right shift' (“décalage binaire à droite”).
# Cela revient à diviser par 2, mais bien plus rapide en interne.
# On fait cela car chaque changement de lettre compte pour 1 dans chaque string, donc le total des écarts est le double du nombre minimal de modifications à faire.
print(ans >> 1)  # On affiche réponse finale (nombre minimal de modifications à effectuer pour rendre les chaînes convertibles en anagrammes)

# Fin du script