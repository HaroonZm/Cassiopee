# AOJ 1209: Square Coins
# Python3 2018.7.19 bal4u

# La liste 'dp' sert à mémoriser le nombre de façons d'exprimer chaque nombre de 0 à 299
# en utilisant des pièces dont les valeurs sont des carrés parfaits (1, 4, 9, 16, ..., 289).
# On l'initialise avec la valeur 1, car il existe exactement 1 façon de former 0 :
# en n'utilisant aucune pièce (c'est l'élément neutre pour l'addition).
dp = [1] * 300  # Crée une liste de 300 éléments, chacun étant initialisé à 1.

# On souhaite remplir la liste 'dp' pour connaître le nombre de façons d'obtenir chaque somme.
# On va donc considérer chaque valeur de pièce qui est un carré parfait, de 2^2 à 17^2 inclus.
for i in range(2, 18):  # On commence à 2 parce que 1^2 a déjà été inclus dans l'initialisation.
    # Pour chaque montant possible (j), on va mettre à jour dp[j]
    # afin d'y additionner toutes les façons de former (j - i^2), c'est-à-dire en ajoutant une pièce de i^2.
    for j in range(i ** 2, 300):  # On commence à i^2 car on ne peut pas former une somme inférieure à i^2 en incluant une pièce de valeur i^2.
        dp[j] += dp[j - i ** 2]  # On ajoute le nombre de façons de former j-i^2 à dp[j].
        # Ainsi, si on peut faire j-i^2 de plusieurs façons, alors prendre chacune de ces façons et ajouter une pièce i^2 donne une nouvelle façon de faire j.

# On passe ensuite à la gestion de la saisie utilisateur.
# On va faire cela dans une boucle infinie qui sera interrompue par une condition d'arrêt explicite.
while True:  # Boucle qui va se répéter indéfiniment, jusqu'à rencontrer le mot-clé 'break'.
    # Lire la prochaine entrée de l'utilisateur, supposée être un entier.
    n = int(input())  # 'input()' lit une ligne, 'int()' convertit la chaîne en entier.
    if n == 0:  # Si l'utilisateur saisit 0, cela signifie qu'on doit arrêter le programme.
        break  # On sort immédiatement de la boucle grâce à 'break'.
    # Si la saisie n'est pas 0, on affiche le nombre de façons de former ce nombre n
    # avec des pièces qui sont des carrés parfaits en regardant dp[n].
    print(dp[n])  # Affiche la réponse pour la valeur lue.