# Boucle principale : On demande d'abord combien de cas de test on souhaite traiter.
# La fonction input() récupère une ligne saisie par l'utilisateur, généralement le nombre de cas.
# int() convertit cette entrée en entier.
# range(int(input())) crée un itérable s'étendant de 0 jusqu'à ce nombre exclus (donc répétition du bloc pour chaque cas).
for _ in range(int(input())):
    # On lit une ligne de deux entiers séparés par un espace.
    # input() récupère une ligne au clavier.
    # split() découpe la chaîne sur les espaces : -> liste de deux chaînes
    # map(int, ...) applique int à chacun des éléments de la liste, donc conversion en entiers.
    # On assigne ces deux entiers aux variables p et q.
    p, q = map(int, input().split())
    # On initialise une variable c qui sert de compteur. Elle compte les solutions trouvées.
    # Elle commence à 0 car aucune solution n'a été trouvée au début.
    c = 0
    # Boucle externe sur la variable i, qui va de 0 jusqu'à 141 inclus :
    # range(142) crée un intervalle d'entiers de 0 à 141.
    for i in range(142):
        # Boucle interne sur la variable j, également de 0 à 141 inclus.
        for j in range(142):
            # On teste trois conditions enchaînées avec "and":
            # 1. (i > 0 or j > 0) : On s'assure que la paire (i, j) n'est pas (0, 0),
            #    donc il faut au moins l'un des deux qui soit strictement positif.
            # 2. (j * p + i * q) % (j * j + i * i) == 0 : On teste si le numérateur est divisible
            #    par le dénominateur sans reste, c'est-à-dire que le reste de la division est 0.
            #    % est l'opérateur "modulo", qui retourne le reste d'une division entière.
            # 3. (j * q - i * p) % (j * j + i * i) == 0 : Même logique ici, mais numérateur différent.
            if (i > 0 or j > 0) and (j * p + i * q) % (j * j + i * i) == 0 and (j * q - i * p) % (j * j + i * i) == 0:
                # Si toutes les conditions sont remplies, on a trouvé une solution valide, donc on incrémente le compteur.
                c += 1
    # Après les deux boucles, on a fini de compter toutes les occurrences qui satisfont la condition.
    # On affiche un résultat selon la valeur du compteur c.
    # Si c < 5 (donc moins de 5 solutions), on affiche la lettre 'P', sinon 'C'.
    # print() affiche la chaîne fournie à l'utilisateur.
    print('P' if c < 5 else 'C')