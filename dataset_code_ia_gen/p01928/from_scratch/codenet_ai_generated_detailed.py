import sys
sys.setrecursionlimit(10**7)

def can_nest(inner, outer):
    """
    Vérifie si la poupée 'inner' peut être rangée directement dans la poupée 'outer'
    après rotation.
    Les dimensions sont triées pour permettre une comparaison simple (chaque côté doit être strictement plus petit).
    """
    inner_sorted = sorted(inner)
    outer_sorted = sorted(outer)
    for i in range(3):
        if inner_sorted[i] >= outer_sorted[i]:
            return False
    return True

def solve(dolls):
    """
    Résout le problème de minimisation du volume total visible.
    """
    N = len(dolls)
    # Pré-calcul des volumes
    volumes = [x*y*z for (x,y,z) in dolls]

    # Construisons le graphe des possibilités d'emboîtage : i -> j si i peut être mis dans j
    can_store = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and can_nest(dolls[i], dolls[j]):
                can_store[i][j] = True

    # DP avec mémoïsation pour chaque poupée : volume minimale visible si poupée i est l'extérieur
    # On choisit un enfant j qui est directement emboité dans i, ou aucun
    memo = [-1]*N
    def dp(i):
        if memo[i] != -1:
            return memo[i]
        res = volumes[i]  # cas où on ne range rien dans i
        for j in range(N):
            if can_store[j][i]:
                # On essaye de ranger j dans i et le reste ailleurs
                # Mais on doit s'assurer que j ne contient pas déjà quelqu'un car une poupée ne peut contenir qu'une autre poupée (mais j peut contenir elle-même quelqu'un)
                # La contrainte interdit une poupée d'emboiter + de 1 poupée directement, mais elle permet qu'une poupée contenant une poupée soit rangée dans une autre.
                # Ici on essaie d'emboiter j directement dans i, donc ok.
                # Le volume visible total sera : volume de i + volume visible de j emboité (donc invisible) n'est plus compté. Ce qu’il faut c’est:
                # en fait, le volume visible si i emboîte j est volume[i] + la somme des volumes visibles des poupées non emboitées dans i et j et les autres.
                # Mais on peut raisonner du point de vue d’un arbre d’emboîtage: on cherche à construire un emboîtement maximum minimisant la somme des visibles.
                # Ici on va utiliser une approche sur un graphe de dépendances.

                # Pour la formulation dp, nous devons considérer que la poupée i contient la poupée j.
                # On considère dp comme la valeur minimale visible de la poupée i (en emboitant au maximum)

                # Le volume vu est volume[i] + somme des volumes visibles des poupées non emboitées dans i ou j.
                # Mais dans dp, on cherche la meilleure valeur de i -> on doit "soustraire" le volume visible de j, c’est-à-dire empiler j.

                # Il faut donc aussi considérer que pq on emboite j dans i, on ajoute volume[i] mais on ne compte pas le volume de j (car elle est invisible).

                # dp(i) = min over j emboité dans i (volume[i] + dp(j)) mais dp(j) correspond au volume visible de sous-arbre avec j comme racine

                # Cependant, on doit éviter de considérer la même poupée dans plusieurs branches (on doit construire un matching maximum)

                # Ce problème est classique de "emboîtage" que l'on peut résoudre par un algorithme de matching maximum dans un graphe biparti.

                # Ici, la solution consiste à modéliser le problème comme un maximum matching dans un graphe biparti où:
                # - Les noeuds du côté gauche sont les poupées "contenu" (rangées)
                # - Les noeuds du côté droit sont les poupées "contenant"

                # Chaque arête i->j existe si la poupée i peut être emboîtée dans j.

                # Le volume visible total = somme des volumes des poupées qui NE sont PAS contenues dans une autre.

                pass
        memo[i] = res
        return res

    # En fait, reformulons:
    # Le problème revient à trouver un matching maximum entre poupées emboîtables où une poupée ne peut contenir qu'une poupée,
    # Afin de minimiser la somme de volumes visibles = somme de volumes des poupées non contenues.

    # Donc, on construit un graphe biparti G = (U,V,E) avec U=V={poupées}
    # Arête u->v si u peut être rangé dans v.

    # On cherche un matching maximum dans ce graphe.

    # Chaque poupée contenant une autre la rend invisible.

    # Volume total visible = somme des volumes - somme des volumes des poupées emboitées (car elles sont invisibles).

    # Problème: Comment maximiser la somme du volume des poupées emboitées?

    # Chaque arête (u,v) dans le matching correspond à emboîter u dans v.
    # On veut un matching maximum GRADEL avec somme poids des pôles U (poupées emboîtées) maximisée.
    # Chaque poupée peut être emboitée au plus une fois et emmboîter au plus une autre (les paires sont uniques).

    # Cela correspond à trouver un matching maximum pondéré avec poids = volume de u (la poupée emboitée).

    # On construit un graphe biparti pondéré :
    # Côté gauche : poupées emboitables (contenues)
    # Côté droite : poupées pouvant être contenant
    # Arête (i,j) avec poids = volumes[i] si i peut être rangé dans j

    # On cherche un maximum matching maximum poids.

    # Là, on applique un algorithme d'affectation ou maximum weighted matching.

    # Limitation: posssible N=100, on peut faire algorithme Hungarian en O(N^3) = 1e6 ce qui est acceptable.

    # Construction du graphe biparti:
    U = list(range(N))
    V = list(range(N))
    cost = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and can_store[i][j]:
                # poids = volume[i], poids positif car on veut maximiser la somme des volumes emboités
                cost[i][j] = volumes[i]

    # Implementation de l'algorithme hongrois (Hungarian) pour maximum weighted bipartite matching
    # Entree: matrice coût cost avec N,N taille
    # Sortie: maximum poids matching

    def hungarian(matrix):
        n = len(matrix)
        u = [0]*(n+1)
        v = [0]*(n+1)
        p = [0]*(n+1)
        way = [0]*(n+1)

        for i in range(1,n+1):
            p[0] = i
            j0 = 0
            minv = [float('inf')]*(n+1)
            used = [False]*(n+1)
            while True:
                used[j0] = True
                i0 = p[j0]
                j1 = 0
                delta = float('inf')
                for j in range(1,n+1):
                    if not used[j]:
                        cur = -matrix[i0-1][j-1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(n+1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break
        # p[j] = i signifie que j dans V est apparié avec i dans U
        # i,j indexés à partir de 1 dans l’algorithme
        # calcul du coût total
        match = [-1]*n
        for j in range(1,n+1):
            if p[j] != 0:
                match[p[j]-1] = j-1
        value = 0
        for i in range(n):
            if match[i] != -1:
                value += matrix[i][match[i]]
        return value, match

    # Calcul du poids max matching (somme des volumes poupées emboîtées)
    max_emboited_volume, matching = hungarian(cost)

    # Volume total
    total_volume = sum(volumes)

    # Résultat : somme volumes poupées visibles = total - volumes emboîtés
    return total_volume - max_emboited_volume

def main():
    input = sys.stdin.readline
    while True:
        N_line = input()
        if not N_line:
            break
        N_line = N_line.strip()
        if N_line == '0':
            break
        N = int(N_line)
        dolls = []
        for _ in range(N):
            x,y,z = map(int, input().split())
            dolls.append((x,y,z))
        ans = solve(dolls)
        print(ans)

if __name__ == "__main__":
    main()