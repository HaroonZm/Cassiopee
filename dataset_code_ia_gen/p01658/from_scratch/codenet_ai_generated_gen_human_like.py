import sys
sys.setrecursionlimit(10**7)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

def can_eat(r, c, eaten):
    # En haut doit être vide ou hors plateau
    if r > 0 and (r-1, c) not in eaten:
        return False
    # Au moins un côté gauche ou droite vide ou hors plateau
    if (c == 0 or (r, c-1) in eaten) or (c == N-1 or (r, c+1) in eaten):
        return True
    return False

def toggle(r, c, state, eaten):
    # Pour toutes les positions adjacentes, si non mangés, inversion du goût
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < M and 0 <= nc < N and (nr,nc) not in eaten:
            state[nr][nc] ^= 1

def dfs(state, eaten, memo):
    key = tuple(tuple(row) for row in state), tuple(sorted(eaten))
    if key in memo:
        return memo[key]
    res = 0
    for r in range(M):
        for c in range(N):
            if (r,c) not in eaten and can_eat(r, c, eaten):
                new_state = [row[:] for row in state]
                new_eaten = eaten | {(r,c)}
                gain = 1 if state[r][c] == 1 else 0
                toggle(r, c, new_state, eaten)
                tmp = gain + dfs(new_state, new_eaten, memo)
                if tmp > res:
                    res = tmp
    memo[key] = res
    return res

print(dfs(board, set(), dict()))