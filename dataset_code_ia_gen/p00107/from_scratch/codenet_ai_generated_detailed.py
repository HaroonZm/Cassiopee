# Programme pour déterminer si Jerry peut passer le fromage à travers chaque trou

import math

def can_pass_through(R, A, B, C):
    """
    Détermine si la pièce de fromage de dimensions A x B x C peut passer
    à travers un trou circulaire de rayon R sans toucher.
    
    On considère que le fromage peut être orienté dans n'importe quelle direction.
    Pour cela, on calcule la plus petite diagonale possible de la pièce (à travers
    une quelconque face ou orientation).
    
    La condition est que le diamètre de la section transversale minimale du
    parallélépipède puisse passer dans le trou.
    
    Mathematiquement, pour un parallélépipède rectangle, l'encombrement minimal
    que l'on doit faire passer dans le trou est la plus petite diagonale parmi les
    projections possibles, mais pour simplifier, on utilise la diagonale de la plus
    petite face (côté à côté), car le trou est circulaire.
    
    En fait, ici, puisqu'on peut orienter le fromage dans n'importe quel angle,
    le rayon minimal nécessaire est la moitié de la diagonale de l'arête la plus
    longue possible projetée.
    
    Néanmoins, la solution la plus simple est :
    - Calculer la plus grande longueur diagonale du parallélépipède : d = sqrt(A**2 + B**2 + C**2)
    - Pour passer complètement par un trou circulaire, il faut que le diamètre maximal soit inférieur à 2*R
    - Or, le plus grand diamètre à faire passer est la plus grande diagonale du parallélépipède.
    - Mais le problème précise qu'on considère uniquement le passage par rotation, donc on peut choisir l'orientation comme on veut.
    
    On doit donc trouver le diamètre minimal du plus petit cercle capable de faire passer le parallélépipède.
    
    Le problème est de trouver la section la plus petite maximale du fromage à toute orientation (place la pièce pour minimiser la section transversale).
    
    Finalement, on peut s'en tenir a la méthode mentionnée dans d'autres sources similaires:
    - On calcule la diagonale de la face la plus grande (car il est plus simple pour passer à plat)
    - Et on compare la diagonale de la face min entre (A,B), (B,C), (A,C) aux rayons.
    
    En résumé, le critère retenu dans ce type de problème est :
    Le fromage peut passer si 2*R >= min des diagonales des faces (min diagonal)
    
    C'est à dire, s'il existe une orientation dans laquelle il passe, alors il passe.
    
    On calcule les diagonales des trois faces et on prend la plus courte.
    Si le diamètre du trou (2*R) est au moins égal à cette diagonale minimale, alors OK.
    
    Sinon, NA.
    """
    # Calcul des diagonales des faces (2D)
    d1 = math.sqrt(A**2 + B**2)
    d2 = math.sqrt(B**2 + C**2)
    d3 = math.sqrt(A**2 + C**2)
    
    min_diag = min(d1, d2, d3)
    diameter = 2*R
    
    return diameter >= min_diag

def main():
    while True:
        # Lecture des dimensions A, B, C
        line = input().strip()
        if line == "":
            continue
        A, B, C = map(int, line.split())
        
        # Condition de fin
        if A == 0 and B == 0 and C == 0:
            break
        
        n = int(input().strip())  # nombre de trous
        radii = []
        for _ in range(n):
            R = int(input().strip())
            radii.append(R)
        
        # Pour chaque trou, évaluer si le fromage peut passer
        for R in radii:
            if can_pass_through(R, A, B, C):
                print("OK")
            else:
                print("NA")

if __name__ == "__main__":
    main()