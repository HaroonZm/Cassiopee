# Définition de la fonction i1 qui lit une entrée utilisateur, la convertit en entier, puis la retourne.
# Cela s'utilise souvent pour récupérer un seul entier à la fois.
def i1():
    # input() lit l'entrée utilisateur sous forme de chaîne de caractères (string).
    # int() convertit cette chaîne de caractères en un entier (integer).
    return int(input())

# Définition de la fonction i2 qui lit une ligne d'entrée,
# divise la chaîne d'entrée en morceaux selon les espaces,
# convertit chaque morceau en entier, puis retourne la liste de ces entiers.
def i2():
    # input() lit la chaîne entrée par l'utilisateur.
    # split() découpe la chaîne en morceaux en utilisant l'espace comme séparateur.
    # La compréhension de liste [int(i) for i in ...] parcourt chaque morceau et le convertit en entier.
    return [int(i) for i in input().split()]

# Appel de la fonction i2 pour récupérer la première ligne d'entrée,
# qui contient deux entiers. L'affectation multiple permet de stocker
# le premier entier dans k et le second dans q.
[k, q] = i2()

# Appel de i2 pour lire la deuxième ligne qui contient probablement 'k' entiers.
# On stocke cette liste dans la variable d.
d = i2()

# Début d'une boucle qui va s'exécuter q fois, où chaque itération traitera une requête.
for i in range(q):
    # À chaque itération, on lit une nouvelle ligne d'entrée contenant trois entiers :
    # n, x, m. On utilise à nouveau i2 et l'affectation multiple.
    [n, x, m] = i2()
    
    # Initialisation d'une liste vide di, qui contiendra le reste de chaque élément de d modulo m.
    di = []
    
    # Initialisation d'une liste vide dz, qui contiendra soit un 1 si l'élément de d est divisible par m,
    # soit un 0 sinon. C'est fait pour compter les éléments multiples de m.
    dz = []
    
    # Boucle qui parcourt chaque élément de d.
    for i in d:
        # Calcul du reste (modulo) de i divisé par m.
        # L'opérateur % donne le reste après division entière.
        di.append(i % m)  # On ajoute ce reste à la liste di.
        
        # On vérifie si i est divisible par m.
        if i % m == 0:
            # Si le reste est zéro, i est divisible par m. On ajoute 1 à la liste dz.
            dz.append(1)
        else:
            # Si ce n'est pas le cas, on ajoute 0 à dz.
            dz.append(0)
    
    # Calcul de la nouvelle valeur de x. 
    # (n-1)//k calcule combien de fois on peut soustraire k de (n-1) sans aller en dessous de zéro.
    # Cela donne le nombre de groupes de taille k dans (n-1) éléments.
    # sum(di[:k]) fait la somme des k premiers éléments dans la liste di.
    # On multiplie cette somme par le nombre de groupes, et on l'ajoute à x modulo m.
    x = ((n - 1) // k) * sum(di[:k]) + x % m
    
    # Si (n-1) % k n'est pas nul (c'est-à-dire qu'il reste quelques éléments après avoir retiré tous les groupes de k),
    # alors on ajoute à x la somme des premiers (n-1)%k éléments de di.
    if (n - 1) % k:
        x += sum(di[:(n - 1) % k])
    
    # Calcul de la réponse : ans.
    # n-1 est le nombre d'éléments moins 1.
    # x//m donne combien de fois x contient m (division entière).
    # ((n-1)//k) * sum(dz[:k]) calcule pour chaque groupe de k éléments,
    # le nombre de divisibles par m dans les k premiers éléments de dz, puis multiplie par le nombre de groupes.
    ans = n - 1 - x // m - ((n - 1) // k) * sum(dz[:k])
    
    # Encore une fois, si il reste des éléments, on enlève aussi à ans le nombre de divisibles par m
    # parmi les premiers éléments restants (n-1)%k éléments.
    if (n - 1) % k:
        ans -= sum(dz[:(n - 1) % k])
    
    # Affichage de la réponse pour la requête courante.
    print(ans)