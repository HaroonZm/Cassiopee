N = 8  # nombre de dames à poser, classique !
n = int(input())  # n = nombre de positions préremplies

# Voilà les tableaux pour la solution
raw = [-1] * N  # -1: pas de dame, sinon, colonne de la dame à la ligne i
col = [0]*N   # 0 : libre, 1 : occupé
dpos = [0]*(2*N-1)  # diagonale /
dneg = [0]*(2*N-1)  # diagonale \

def put_queen(row):
    # Si on a placé toutes les dames, bingo !
    if row == N:
        return True
    elif raw[row] != -1:
        # Si déjà forcé, on passe à la suite
        return put_queen(row+1)
    else:
        # On essaye sur chaque colonne
        for column in range(N):
            if col[column] or dpos[row+column] or dneg[row-column+N-1]:
                # ocp, on skip
                continue
            # Ok, on place ici
            raw[row] = column
            col[column] = 1
            dpos[row+column] = 1
            dneg[row-column+N-1] = 1
            # On passe à la ligne suivante
            if put_queen(row+1):
                return True
            # sinon, retour en arrière, dommage :/
            raw[row] = -1
            col[column] = 0
            dpos[row+column] = 0
            dneg[row-column+N-1] = 0
        # Pas trouvé ici
        return False

def output_result():
    # On affiche le plateau
    for i in range(N):
        l = ['.'] * N
        if raw[i] >= 0:
            l[raw[i]] = 'Q'
        else:
            # normalement, ça n'arrive pas
            pass
        print(''.join(l))

# Prépositions forcées
for _ in range(n):
    x, y = map(int, input().split())
    raw[x] = y
    col[y] = 1
    dpos[x+y] = 1
    dneg[x-y+N-1] = 1

# Et c'est parti
put_queen(0)
output_result()