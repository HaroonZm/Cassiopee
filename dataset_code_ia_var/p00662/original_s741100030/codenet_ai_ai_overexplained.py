# Démarrer une boucle infinie qui ne s'arrêtera que lorsqu'une condition spécifique sera remplie
while True:
    # Lire une ligne depuis l'entrée standard (input utilisateur)
    # La fonction input() retourne une chaîne de caractères saisie par l'utilisateur (par exemple "3 3 3 0 0 0")
    # La fonction split() découpe cette chaîne en une liste de sous-chaînes à chaque espace (par exemple ['3', '3', '3', '0', '0', '0'])
    # map(int, ...) convertit chaque élément de la liste en entier car input() donne des chaînes de caractères
    # Enfin, list(...) transforme l'objet map en une vraie liste d'entiers
    ns = list(map(int, input().split()))
    
    # Vérifier si tous les éléments de la liste ns valent zéro
    # La fonction any(ns) retourne True si au moins un élément de ns est non nul
    # Donc, 'not any(ns)' est vrai uniquement si tous les éléments sont nuls (c'est-à-dire tous égaux à 0)
    if not any(ns):
        # Si tous les éléments sont nuls, on sort de la boucle avec break
        break
    
    # Additionner certains éléments des deux moitiés de la liste ns pour former trois variables a, b, c
    # ns[0] est le premier nombre, ns[3] est le quatrième, etc.
    # Cela simule une addition groupe-à-groupe
    a = ns[0] + ns[3]  # Premier groupe (1er + 4ème)
    b = ns[1] + ns[4]  # Deuxième groupe (2ème + 5ème)
    c = ns[2] + ns[5]  # Troisième groupe (3ème + 6ème)
    
    # Calculer la division entière et le reste de chaque somme (a, b, c) par 3
    # Cela revient à compter combien de "groupes de 3" on peut faire dans chaque somme, et combien il en reste
    # // est l'opérateur de division entière, % donne le reste de la division
    av = a // 3  # Nombre de groupes de 3 complets dans a
    ar = a % 3   # Reste après avoir formé des groupes de 3 dans a
    bv = b // 3  # Idem pour b
    br = b % 3
    cv = c // 3  # Idem pour c
    cr = c % 3
    
    # On va maintenant déterminer combien de groupes complets et partiels on peut former
    # et afficher un nombre selon certaines combinaisons
    
    # Si tous les restes (ar, br, cr) sont égaux à 0 (c’est-à-dire, toutes les quantités étaient des multiples de 3)
    if max(ar, br, cr) == 0:
        # L'addition des groupes complets pour a, b, c donne le résultat total et il n'y a pas de reste
        print(av + bv + cv)
    
    # Si le plus grand reste parmi (ar, br, cr) est 1 (il y a donc au moins un groupe partiel qui n'atteint pas 3)
    elif max(ar, br, cr) == 1:
        # Le résultat est la somme des groupes complets, plus le plus petit reste (qui est forcément 0 ou 1)
        print(av + bv + cv + min(ar, br, cr))
    
    # Si le plus grand reste est 2 (possibilité de plusieurs restes égaux à 2)
    elif max(ar, br, cr) == 2:
        # Compter combien de groupes ont un reste de 2
        reste_2_count = [ar, br, cr].count(2)
        
        # Si tous les groupes ont un reste de 2
        if reste_2_count == 3:
            # On ajoute 2 au total des groupes complets
            print(av + bv + cv + 2)
        
        # Si seulement deux groupes ont un reste de 2
        elif reste_2_count == 2:
            # Pour chaque couple formé du reste et du nombre de groupes complets (xr, xv)
            for xr, xv in ((ar, av), (br, bv), (cr, cv)):
                # Si le reste égal 2 (on veut identifier le groupe qui n’a pas un reste de 2)
                if xr == 2:
                    # On passe au groupe suivant si le reste est 2
                    continue
                # Ici, on a trouvé le groupe dont le reste n’est pas 2
                # S'il n'y a aucun groupe complet dans ce groupe-là
                if xv == 0:
                    # Alors, on ajoute l'entier du reste (qui sera soit 0 soit 1) au total
                    print(av + bv + cv + xr)
                else:
                    # Sinon, on ajoute simplement 1 au total des groupes complets
                    print(av + bv + cv + 1)
                # On a traité le groupe unique qui n'a pas reste 2, on sort de la boucle
                break
        
        # Si un seul groupe a un reste de 2 (tous les autres sont à 0 ou 1)
        else:
            # Ici, on ajoute le plus petit reste (parmi 0, 1, 2), à la somme des groupes complets
            print(av + bv + cv + min(ar, br, cr))