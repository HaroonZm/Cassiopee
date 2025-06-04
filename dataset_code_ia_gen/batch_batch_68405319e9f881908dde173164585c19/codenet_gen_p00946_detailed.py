import sys
input = sys.stdin.readline

# Probleme : on a une sequence initiale (1, 2, ..., n).
# On recoit m requetes indiquant un element e_i a deplacer en tete de la sequence.
# Il faut appliquer en ordre toutes ces requetes et afficher la sequence finale.

# Contraintes fortes (n jusqu'a 200000 et m jusqu'a 100000)
# => un simple deplacement O(n) pour chaque requete serait trop lent (O(n*m) ~ 2e10)
# Il faut une structure efficace.

# Approche :
# Chaque element a un "rang" ou "position" dans la sequence.
# Au depart, position[x] = x (pour element x = 1..n)
# Quand on deplace un element e_i en tete, on doit lui attribuer une position plus petite que toutes les autres.
# On peut utiliser un compteur decremente => on attribue une "position virtuelle" plus petite
# Les positions minoreront les precedentes, donc l'ordre final est les elements tries par leur position effective.

# Implementation detaillee :
# - On initialise position[x] = x pour tous x.
# - On initialise cur_pos = 0
# - Pour chaque requete e:
#     on met position[e] = cur_pos
#     on decremente cur_pos de 1 (pour la prochaine mise en tete)
# - Enfin, on trie les elements par position et on affiche dans cet ordre.

def main():
    n, m = map(int, input().split())
    positions = [0] * (n+1)  # positions[elem] = position dans la sequence (position virtuelle)
    for i in range(1, n+1):
        positions[i] = i  # positions initiales

    current_pos = 0  # on commencera a decremente a partir de 0 pour les mises en tete

    for _ in range(m):
        e = int(input())
        # Move e to head: lui donner une position plus petite que toutes les autres
        positions[e] = current_pos
        current_pos -= 1

    # maintenant on a la position virtuelle de chaque element,
    # ceux qui ont une position plus faible sont plus en tete

    # Trier les elements 1..n par position croissante
    elements_sorted = sorted(range(1, n+1), key=lambda x: positions[x])

    # Affichage du resultat
    print('\n'.join(map(str, elements_sorted)))

if __name__ == "__main__":
    main()