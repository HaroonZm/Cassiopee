import math  # On importe le module math qui contient des fonctions mathématiques de base, notamment la racine carrée.

def sieve(n):
    # 'sieve' est une fonction qui génère une liste représentant la primalité pour tous les nombres de 0 à n inclus.
    # Les indices de la liste correspondent aux entiers; une valeur de 1 à l'indice i signifie que i est premier, 0 signifie non premier.
    
    prime = [0, 0]  # On initialise une liste nommée 'prime': 0 (faux) aux indices 0 et 1 car 0 et 1 ne sont pas premiers.
    
    # On ajoute à la liste 'prime' une suite de 1 (vrai); pour chaque i de 2 à n inclus:
    prime += [1 for i in range(n - 1)]  # Ainsi, les indices ≥2 sont initialisés à 1 par défaut, supposés être premiers.
    
    # 'ub' contiendra la borne supérieure de la boucle, soit racine carrée de n (on ajoute 1 pour inclure l'entier supérieur). 
    ub = math.sqrt(n) + 1  # math.sqrt(n) donne la racine carrée de n.
    
    d = 2  # On commence à 2, le premier nombre premier.
    # On effectue la recherche des multiples de chaque nombre premier jusqu'à la racine carrée de n.
    while d <= ub:  # Tant que d est inférieur ou égal à ub (racine carrée de n arrondie à l'entier supérieur).
        if prime[d] == 0:  # Si d n'est pas premier (déjà marqué comme non premier)... 
            d += 1  # ... on passe simplement au nombre suivant.
            continue  # On saute le reste de cette itération et on recommence la boucle.
        prod = 2  # On va multiplier d successivement par 2, 3, 4, ..., pour marquer leur produit comme non premier.
        while d * prod <= n:  # Tant que le produit (d * prod) ne dépasse pas n...
            prime[d * prod] = 0  # ... on marque d * prod comme non premier en mettant un 0 à cet indice dans la liste.
            prod += 1  # On passe au multiplicateur suivant pour trouver les prochains multiples.
        d += 1  # Une fois tous les multiples de d traités, on continue avec le nombre suivant.
    return prime  # On retourne la liste 'prime', dont chaque indice i indique si i est premier.

# On appelle la fonction sieve pour générer la primalité jusqu'à 1299709, qui est un nombre suffisamment grand pour le contexte du problème.
prime = sieve(1299709)

# On démarre une boucle infinie pour traiter les entrées utilisateur continuellement.
while 1:  # 1 est toujours vrai en Python ; cette boucle ne s'arrêtera donc que par un break explicite.
    k = int(raw_input())  # On lit une valeur entière saisie par l'utilisateur grâce à raw_input, puis on la convertit en int.
    if k == 0:  # Si la valeur saisie est 0...
        break  # ... on sort de la boucle et le programme s'arrête.
    l = r = k  # On initialise deux variables, l et r, à la valeur de k; elles vont servir à chercher les nombres premiers autour de k.
    
    # On cherche le plus grand nombre premier strictement plus petit ou égal à k.
    while prime[l] == 0:  # Tant que l n'est pas un nombre premier...
        l -= 1  # ... on décrémente l pour vérifier le nombre précédent.
    
    # On cherche le plus petit nombre premier supérieur ou égal à k.
    while prime[r] == 0:  # Tant que r n'est pas un nombre premier...
        r += 1  # ... on incrémente r pour vérifier le nombre suivant.
    
    # 'l' est le plus grand nombre premier ≤ k, 'r' est le plus petit nombre premier ≥ k.
    # La distance entre ces deux nombres premiers est (r - l).
    # Mais on cherche le nombre d'entiers entre les deux premiers, c’est-à-dire r - l + 1 - 1, soit (r-1) - (l+1) + 2 (formule d’origine).
    print((r - 1) - (l + 1) + 2)  # On affiche le résultat, c’est-à-dire la taille de l’intervalle entre les deux nombres premiers entourant k.