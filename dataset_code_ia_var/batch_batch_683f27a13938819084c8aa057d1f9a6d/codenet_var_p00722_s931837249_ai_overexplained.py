import sys  # Importe le module système pour utiliser sys.stdin pour la saisie

# Définir une constante représentant la limite supérieure jusqu'à laquelle les nombres premiers seront marqués.
MAX = 1000000  # Ici, on fixe la limite à un million (1_000_000).

# Créer une liste appelée 'prime' de taille MAX pour tenir l'information sur la primalité des entiers.
# Chaque case représente un nombre de 1 à MAX, où la case d'indice i représente le nombre i+1.
# On initialise toutes les cases à -1 pour indiquer que l'état de primalité n'est pas encore déterminé.
prime = [-1] * MAX

# Initialisation de la variable 'i' à 2, car 2 est le plus petit nombre premier.
i = 2

# Cette boucle 'while' va parcourir tous les entiers de 2 jusqu'à MAX-1 inclus.
while i < MAX:
    # Vérifie si le nombre (i) n'a pas encore été traité (sa case est -1).
    if prime[i - 1] == -1:
        # Marque le nombre (i) comme premier en mettant 0 à la position correspondante de la liste.
        prime[i - 1] = 0  

        # Simule le crible d'Ératosthène en itérant sur les multiples de i pour les marquer comme non premiers.
        temp = i * 2  # Commence avec le double de i car c'est le premier multiple non égal à i.
        while temp < MAX:
            # Marque chaque multiple de i comme non premier en mettant 1 à la position correspondante.
            prime[temp - 1] = 1
            # Incrémente temp de i pour passer au prochain multiple.
            temp += i
    # Si on traite le chiffre 2, le nombre premier suivant est 3 (on passe à 3).
    if i == 2:
        i += 1
    else:
        # Après 2, tous les autres nombres premiers sont impairs donc on saute les nombres pairs.
        i += 2

# Boucle infinie pour traiter plusieurs cas de test jusqu'à ce qu'une condition d'arrêt soit atteinte.
while True:
    # Lit une ligne entière provenant de la saisie standard, la découpe et la convertit en trois entiers :
    a, d, n = map(int, sys.stdin.readline().split())

    # Condition d'arrêt : si a, d et n valent tous zéro on arrête la boucle.
    if a == 0 and d == 0 and n == 0:
        break

    # Initialise le compteur de nombres premiers trouvés dans la progression.
    count = 0

    # Une boucle pour générer les termes de la suite arithmétique et compter les nombres premiers.
    while True:
        # Vérifie si le nombre 'a' actuel est premier : si prime[a-1] vaut 0, c'est un nombre premier.
        if prime[a - 1] == 0:
            count += 1  # Incrémente le compteur si 'a' est premier.

        # Vérifie si nous avons déjà trouvé 'n' nombres premiers.
        if count < n:
            # Si ce n'est pas le cas, passer au prochain terme de la progression en ajoutant 'd'.
            a = a + d
        else:
            # Sinon, casser la boucle car on a trouvé assez de nombres premiers.
            break
    # Affiche le n-ième nombre premier trouvé dans la progression arithmétique.
    print a  # Utilise print sans parenthèses car cela fonctionne avec Python 2.