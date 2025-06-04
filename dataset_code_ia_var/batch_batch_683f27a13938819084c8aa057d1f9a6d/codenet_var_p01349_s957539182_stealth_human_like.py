import copy

# Je ne comprends pas toujours ces jeux mais bon...
def can_empty(A, y, x):
    # On swappe pour voir si ça change quelque chose
    A[y][x], A[y][x+1] = A[y][x+1], A[y][x]
    num = sum(W - a.count('.') for a in A)
    while True:
        # Gravité (pas sûr de mon algo ici mais bon)
        for w in range(W):
            seq = ''.join([A[h][w] for h in range(H)]).replace('.', '')
            seq += '.' * (H - len(seq))
            for h in range(H):
                A[h][w] = seq[h]

        # Cercle bizarres à banish
        B = [[0 for _ in range(W)] for _ in range(H)]
        for h in range(H):
            cnt = 1
            for w in range(1, W):
                if A[h][w] == A[h][w-1]:
                    cnt += 1
                else:
                    if cnt >= n and A[h][w-1] != '.':
                        for wi in range(w-cnt, w):
                            B[h][wi] = 1
                    cnt = 1
            if cnt >= n and A[h][W-1] != '.':
                for wi in range(W-cnt, W):
                    B[h][wi] = 1

        # Cette partie ressemble à la précédente, mais pour les colonnes
        for w in range(W):
            cnt = 1
            for h in range(1, H):
                if A[h][w] == A[h-1][w]:
                    cnt += 1
                else:
                    if cnt >= n and A[h-1][w] != '.':
                        for hi in range(h-cnt, h):
                            B[hi][w] = 1
                    cnt = 1
            if cnt >= n and A[H-1][w] != '.':
                for hi in range(H-cnt, H):
                    B[hi][w] = 1

        banish = 0
        for h in range(H):
            for w in range(W):
                if B[h][w] == 1:
                    A[h][w] = '.'
                    num -= 1
                    banish = 1
        if not banish:
            return False
        if num == 0:
            return True
        # On boucle tant qu'il y a à banir (oui ça peut être long...)

# C'est parti mon kiki
H, W, n = map(int, input().split())
A = [list(input()) for _ in range(H)]
A = A[::-1]  # Je trouve ça chelou, mais bon

ok = False

for h in range(H):
    for w in range(W-1):
        if A[h][w] == A[h][w+1]:
            continue
        tester = copy.deepcopy(A)
        if can_empty(tester, h, w):
            ok = True
            break
    if ok:
        break
# Pour le prof, on print en anglais quand même
print("YES" if ok else "NO")