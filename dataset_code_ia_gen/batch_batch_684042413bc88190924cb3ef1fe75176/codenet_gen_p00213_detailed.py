import sys

def solve():
    input = sys.stdin.readline
    while True:
        # Lecture de X, Y, n
        line = input()
        if not line:
            break
        X, Y, n = map(int, line.split())
        if X == 0 and Y == 0 and n == 0:
            break

        # Lecture des informations (b_i,k_i) des acheteurs
        buyer_info = {}
        for _ in range(n):
            b, k = map(int, input().split())
            buyer_info[b] = k

        # Lecture du plan s (Y lignes de X cases)
        # s[y][x] correspond à la case (x,y) avec x de 0 à X-1, y de 0 à Y-1
        s = [list(map(int, input().split())) for _ in range(Y)]

        # Constantes
        INF = 10**9

        # La sortie recherchée est une répartition de la grille en rectangles.
        # Chaque rectangle représente une zone achetée par un acheteur avec :
        # - une forme rectangulaire (contiguë)
        # - la taille exacte k (déjà donnée)
        # - et au moins un marqueur b dans cette zone sur s.

        # Stratégie:
        # Pour chaque acheteur b:
        #   Chercher tous les rectangles possibles contenant exactement k cases et contenant au moins une cellule avec s[y][x]==b.
        #   Car on sait que pour b, la parcelle doit être un rectangle contenant k cases.
        # Ensuite, essayer toutes les combinaisons possibles de ces rectangles (un par acheteur).
        # Vérifier que ces rectangles forment une partition complète de la parcelle (X*Y).
        # - Si plus d'une solution valide: imprimer NA
        # - Si aucune solution valide: imprimer NA
        # - Sinon, imprimer la solution.

        # Construire une liste de rectangles candidates pour chaque acheteur
        rects = {b: [] for b in buyer_info.keys()}

        # Pré-calcul de zones candidates par acheteur
        # Recense les positions où chaque numéro b est marqué dans s
        positions = {b: [] for b in buyer_info.keys()}
        for y in range(Y):
            for x in range(X):
                bnum = s[y][x]
                if bnum in positions:
                    positions[bnum].append((x,y))

        # Fonction pour vérifier si un rectangle possede au moins un marqueur de l'acheteur
        def has_marker(rect, b):
            x1,y1,x2,y2 = rect
            for (mx,my) in positions[b]:
                if x1 <= mx <= x2 and y1 <= my <= y2:
                    return True
            return False

        # Fonction pour compter la taille du rectangle (x2-x1+1)*(y2-y1+1)
        def size(rect):
            x1,y1,x2,y2 = rect
            return (x2 - x1 +1) * (y2 - y1 +1)

        # Générer tous les rectangles possibles dans la grille, puis filtrer
        # Pour chaque rectangle (x1,y1) -> (x2,y2)
        # Si sa taille correspond à k pour l'acheteur b et contient un marqueur de b
        # Ajouter ce rectangle aux candidats de b
        for b,k in buyer_info.items():
            candidate_rects = []
            for y1 in range(Y):
                for y2 in range(y1, Y):
                    height = y2 - y1 + 1
                    if k % height != 0:
                        continue
                    width = k // height
                    if width > X:
                        continue
                    for x1 in range(X - width +1):
                        x2 = x1 + width -1
                        rect = (x1,y1,x2,y2)
                        if has_marker(rect,b):
                            candidate_rects.append(rect)
            rects[b] = candidate_rects
            # Si aucun rectangle possible, on peut s'arreter
            if not candidate_rects:
                rects[b] = []

        # Si pour quelque acheteur il n'y a pas de rectangle possible, sortie NA immédiate
        if any(len(rects[b]) == 0 for b in buyer_info):
            print("NA")
            continue

        # Il faut tester toute combinaison rects[b1] x rects[b2] x ...
        # et valider qu'elles partitionnent l'intégralité de la grille sans superposition
        # et que la somme des tailles est X*Y

        # Liste des acheteurs dans un ordre fixe pour parcours
        buyers = list(buyer_info.keys())

        # Ensemble des indices pour backtracking
        res = []
        solutions = []
        MAX_SOL = 2  # on va stopper après 2 solutions pour savoir s'il y en a plusieurs

        # Fonction pour vérifier s'il y a recouvrement entre rectangles
        # Pour stocker l'occupation on pleine grille on peut utiliser une matrice booléenne
        def backtrack(i, used_grid):
            if len(solutions) > MAX_SOL:
                return
            if i == len(buyers):
                # Solution trouvée
                solution = []
                for b in buyers:
                    solution.append(res[buyers.index(b)])
                solutions.append(solution)
                return

            b = buyers[i]
            for rect in rects[b]:
                # Tester si rect chevauche déjà utilisé
                x1,y1,x2,y2 = rect
                conflict = False
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        if used_grid[y][x]:
                            conflict = True
                            break
                    if conflict:
                        break
                if conflict:
                    continue
                # marquer rectangle utilisé
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        used_grid[y][x] = True
                res.append(rect)
                backtrack(i+1, used_grid)
                res.pop()
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        used_grid[y][x] = False

        # Préparer une grille booléenne pour marquer occupation
        used_grid = [[False]*X for _ in range(Y)]

        backtrack(0, used_grid)

        # Analyse résultats
        if len(solutions) == 0:
            print("NA")
        elif len(solutions) > 1:
            print("NA")
        else:
            # Une seule solution
            sol = solutions[0]
            # Construire la grille de sortie avec les numéros d'acheteurs
            ans = [[0]*X for _ in range(Y)]
            for i,b in enumerate(buyers):
                rect = sol[i]
                x1,y1,x2,y2 = rect
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        ans[y][x] = b

            # Impression au format demandé (Y lignes de X valeurs)
            for y in range(Y):
                print(' '.join(str(ans[y][x]) for x in range(X)))
if __name__ == "__main__":
    solve()