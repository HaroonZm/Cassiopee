# On cherche le nombre de façons de choisir la hauteur d'un étage (entre A et B)
# telle que le nombre total d'étages (H divisé par la hauteur d'un étage) soit un entier.
# En effet, l'immeuble fait une hauteur H, chaque étage a une hauteur h (A <= h <= B),
# et H doit être divisible par h pour que la hauteur totale soit exactement H.
# On compte donc le nombre de diviseurs de H dans l'intervalle [A, B].

def count_floor_height_options(H, A, B):
    count = 0
    # Pour chaque hauteur possible entre A et B
    for h in range(A, B + 1):
        # On vérifie si h divise H
        if H % h == 0:
            count += 1
    return count

def main():
    # Lecture des données
    H, A, B = map(int, input().split())
    # Calcul et sortie du résultat
    print(count_floor_height_options(H, A, B))

if __name__ == "__main__":
    main()