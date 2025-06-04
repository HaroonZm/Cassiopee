#!/usr/bin/python3

# Crée une liste appelée 'Fact' contenant 100001 éléments (indices 0 à 100000), chacun initialisé à False.
# Cela signifie qu'aucun entier n'a, au départ, été marqué d'une propriété particulière.
Fact = [False for _ in range(10**5+1)]

# Définition de la fonction 'get_fact', qui prend un entier 'm' en argument.
# Cette fonction va déterminer une propriété concernant 'm', en travaillant avec la liste globale 'Fact'.
def get_fact(m):
    # On indique utiliser la variable globale 'Fact', sinon Python considérerait Fact comme locale à la fonction.
    global Fact
    # On initialise la variable 'ans' à 1 (c'est le point de départ de la multiplication).
    ans = 1
    # On parcourt les entiers de 2 jusqu'à la racine carrée entière de 'm', incluse (équivalent à "for i in range(2, sqrt(m) + 1)").
    for i in range(2, int(m**0.5) + 1):
        # On vérifie si 'i' est un diviseur de 'm', i.e., si la division entière de m par i ne laisse pas de reste.
        if m % i == 0:
            # Si 'i' est un diviseur, on multiplie 'ans' par 'i'.
            ans *= i
            # On regarde si 'i' et 'm//i' (le diviseur complémentaire) sont différents pour éviter de multiplier deux fois le même facteur s'ils sont égaux (c'est le cas si m est un carré parfait).
            if i != m // i:
                # On multiplie aussi 'ans' par 'm//i', le diviseur complémentaire.
                ans *= m // i
            # Si à un certain moment, 'ans' devient supérieur ou égal à deux fois 'm', ou si Fact[m//i] est déjà True (ce qui veut dire qu'on a déjà déterminé une certaine propriété pour ce nombre diviseur), alors :
            if ans >= m * 2 or Fact[m // i]:
                # On retourne True pour indiquer que 'm' satisfait la condition recherchée.
                return True
    # Si la boucle se termine sans déclencher de retour prématuré, on retourne False (donc 'm' ne satisfait pas la condition).
    return False

# On crée une liste 'Fact_n' de longueur 100001, initialisée à 0, pour garder un cumul de "vrais" dans 'Fact' jusqu'à l'indice courant (préfix sum).
Fact_n = [0 for _ in range(10**5+1)]
# Pour chaque entier 'i' de 2 à 100000 inclus (on commence à 2 car 0 et 1 n'ont pas de diviseurs proprement dits),
for i in range(2, 10**5 + 1):
    # On utilise la fonction 'get_fact' pour déterminer la propriété de l'entier 'i' et on met à jour 'Fact[i]' avec le résultat.
    Fact[i] = get_fact(i)
    # Si 'Fact[i]' est vrai (True), cela veut dire que 'i' satisfait la propriété recherchée.
    if Fact[i]:
        # On incrémente Fact_n[i] de 1 par rapport à Fact_n[i-1], car un nouvel entier satisfait la propriété.
        Fact_n[i] = Fact_n[i-1] + 1
    else:
        # Sinon, le total de 'True' reste le même que pour l'entier précédent.
        Fact_n[i] = Fact_n[i-1]

# Lecture d'un entier 'Q' depuis l'entrée utilisateur, indiquant combien de requêtes vont être faites.
Q = int(input())
# On prépare une liste 'ret' de longueur Q, remplie de 0, qui va contenir les réponses à chaque requête.
ret = [0 for _ in range(Q)]
# Pour chaque requête (on itère 'Q' fois, avec l'indice 'q' allant de 0 à Q-1 inclus),
for q in range(Q):
    # On lit un entier depuis l'entrée standard pour chaque requête.
    # Cet entier correspond à un certain 'n'.
    # On assigne à ret[q] la valeur de Fact_n[n], qui est le nombre cumulé d'entiers <= n qui satisfont la propriété.
    ret[q] = Fact_n[int(input())]

# On parcourt tous les éléments de la liste 'ret' (qui contient les réponses aux différentes requêtes),
for q in ret:
    # Et on affiche chaque réponse sur sa propre ligne.
    print(q)