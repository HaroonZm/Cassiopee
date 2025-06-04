# Lecture des entrées et résolution du problème Yu-kun Likes Rectangles en Python

# La stratégie est la suivante :
# 1) Lire les matrices A, B et C.
# 2) Chercher toutes les positions (i, j) dans B où le motif C peut s'emboîter complètement.
# 3) Pour chaque position, vérifier si le sous-rectangle de B correspond exactement à C.
# 4) Si oui, calculer la somme des entiers correspondants dans A.
# 5) Gérer le maximum sur toutes les correspondances trouvées.
# 6) Afficher le résultat ou "NA" s'il n'y en a pas.

import sys

def main():
    input = sys.stdin.readline

    # Lecture des dimensions H, W 
    H, W = map(int, input().split())
    
    # Lecture de la matrice A (H x W) des entiers
    A = [list(map(int, input().split())) for _ in range(H)]
    
    # Lecture de la matrice B (H x W) des couleurs (0 ou 1)
    B = [list(map(int, input().split())) for _ in range(H)]
    
    # Lecture des dimensions h, w 
    h, w = map(int, input().split())
    
    # Lecture de la matrice C (h x w) des couleurs (0 ou 1)
    C = [list(map(int, input().split())) for _ in range(h)]
    
    max_score = None  # Aucun score trouvé pour l'instant

    # On parcourt toutes les positions possibles où C peut s'imbriquer dans B
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            # Vérification que le sous-rectangle B[i:i+h][j:j+w] correspond exactement à C
            match = True
            for x in range(h):
                for y in range(w):
                    if B[i + x][j + y] != C[x][y]:
                        match = False
                        break
                if not match:
                    break

            if match:
                # Calculer la somme des éléments correspondants dans A
                score = 0
                for x in range(h):
                    for y in range(w):
                        score += A[i + x][j + y]

                # Mettre à jour le max_score
                if (max_score is None) or (score > max_score):
                    max_score = score

    # Afficher le résultat ou "NA"
    if max_score is None:
        print("NA")
    else:
        print(max_score)

if __name__ == "__main__":
    main()