# Demande à l'utilisateur trois entiers séparés par des espaces et les assigne à N, A, B
N, A, B = map(int, input().split())

# Crée une liste 'h' qui contiendra les points de vie (HP) de chaque monstre. 
# Pour chaque monstre (il y en a N), l'utilisateur doit entrer un nombre, qui est converti en entier et ajouté à la liste.
h = [int(input()) for _ in range(N)]

# Définit une fonction appelée 'fight' qui prend un paramètre 'k'.
# Cette fonction va déterminer si on peut vaincre tous les monstres en 'k' tours ou moins en utilisant l'attaque spéciale.
def fight(k):
    c = k  # Initialise 'c' à la valeur de 'k'. 'c' représente le nombre d'attaques spéciales restantes à utiliser au total.
    for i in h:
        # Pour chaque monstre dans la liste 'h', on récupère ses points de vie initiaux 'i'.
        # On calcule le nombre de dégâts faits à ce monstre par les attaques régulières sur 'k' tours.
        hp = i - B * k  # Chaque tour, tous les monstres reçoivent une attaque régulière de dégâts 'B'.
        # Après 'k' tours, chaque monstre a reçu 'B*k' dégâts, donc on soustrait ça à ses PV de départ.
        if hp > 0:  # Si le monstre a encore des PV après toutes les attaques régulières...
            # Il faut utiliser des attaques spéciales (qui font A dégâts, mais A > B) supplémentaires pour le vaincre.
            # (A-B) est le surcroît de dégâts d'une attaque spéciale par rapport à une normale.
            # Le nombre d'attaques spéciales nécessaires est hp divisé par (A - B), mais il faut arrondir au supérieur.
            # On utilise -(-hp // (A - B)) pour faire une division entière arrondie au supérieur.
            # On soustrait ce nombre d'attaques spéciales du compteur 'c'.
            c -= -(-hp // (A - B))
        if c < 0:
            # Si à tout moment on a utilisé plus d'attaques spéciales que permis ('k'), c'est impossible.
            return False  # On retourne donc False.
    # Si on termine la boucle sans problème, toutes les conditions sont remplies.
    return True  # On retourne True pour indiquer que c'est faisable.

# Initialise la borne inférieure 'lo' à 0 : c'est le plus petit nombre de tours possible.
lo = 0

# Initialise la borne supérieure 'hi' à un très grand nombre (ici 10**9) pour être sûr de couvrir tous les cas possibles.
hi = 10 ** 9

# Lance une boucle de recherche binaire pour trouver la plus petite valeur de 'k' qui rend 'fight(k)' vrai.
while hi - lo > 1:
    # À chaque itération, on prend le milieu entre 'lo' et 'hi'.
    mid = (lo + hi) // 2
    # On appelle la fonction 'fight' avec 'mid' comme argument :
    if fight(mid):
        # Si c'est possible de vaincre tous les monstres en 'mid' tours ou moins,
        # on sait qu'on peut peut-être faire encore mieux, donc on abaisse la borne supérieure à 'mid'.
        hi = mid
    else:
        # Sinon, ce n'est pas possible, donc il faut augmenter le nombre de tours.
        # On remonte la borne inférieure à 'mid'.
        lo = mid

# À la fin de la boucle, la plus petite valeur de 'k' possible est 'hi'.
print(hi)  # On affiche la réponse finale.