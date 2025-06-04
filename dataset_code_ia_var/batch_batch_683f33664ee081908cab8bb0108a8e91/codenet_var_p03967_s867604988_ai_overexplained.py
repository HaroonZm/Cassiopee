# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier.
# La méthode input() affiche une invite (ici vide) et attend que l'utilisateur saisisse un texte, puis appuie sur Entrée. 
# La valeur saisie est alors stockée dans la variable 's' de type str (chaîne de caractères).
s = input()

# Calcule la longueur (c'est-à-dire le nombre total de caractères) de la chaîne 's' et stocke ce nombre entier dans la variable 'l'.
# La fonction len() retourne le nombre d'éléments d'un objet de type séquence ou collection (ici, une chaîne).
l = len(s)

# Compte combien de fois la lettre minuscule 'g' apparaît dans la chaîne 's' et stocke ce nombre entier dans la variable 'g'.
# La méthode count() d'un objet str retourne le nombre d'occurrences non chevauchantes du sous-chaîne donnée ('g' ici) dans la chaîne cible.
g = s.count('g')

# Compte combien de fois la lettre minuscule 'p' apparaît dans la chaîne 's' et stocke ce nombre entier dans la variable 'p'.
# Ici aussi, on utilise la méthode count(), appliquée à la chaîne 's', avec l'argument 'p' pour compter les 'p'.
p = s.count('p')

# Vérifie si le nombre de 'g' est supérieur ou égal au nombre de 'p'.
# L'opérateur >= compare les deux valeurs numériques 'g' et 'p' et retourne True si g est plus grand ou égal à p.
if g >= p:
    # Si la condition ci-dessus est vraie (donc il y a au moins autant de 'g' que de 'p' dans la chaîne):
    # On calcule la différence entre le nombre de 'g' et le nombre de 'p' (c'est-à-dire g - p).
    # Puis on divise cette différence par 2 en utilisant l'opérateur //, qui est la division entière (le résultat est arrondi vers le bas à l'entier le plus proche).
    # On passe ce résultat à la fonction print(), qui affiche la valeur à l'écran.
    print((g - p) // 2)
else:
    # Sinon (c'est-à-dire s'il y a plus de 'p' que de 'g' dans la chaîne):
    # On calcule la différence entre le nombre de 'p' et le nombre de 'g' (soit p - g).
    # Cette différence est divisée par 2, toujours en utilisant la division entière // pour obtenir un résultat sans partie décimale.
    # On met un signe moins devant le résultat pour renvoyer une valeur négative.
    # Ensuite, on affiche cette valeur avec print().
    print(-(p - g) // 2)