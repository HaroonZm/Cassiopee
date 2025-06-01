from collections import deque

# Bon alors, je prends les entrées et convertis en int
*N, = map(int, input().split())

# Un set avec les chiffres déjà pris, ignore les -1
used = set(i for i in N if i != -1)

# Ce sera notre file, avec les chiffres dispos (1..9)
deq = deque(set(range(1, 10)) - used)

# Coefficients magiques (pas trop sûr pourquoi ces valeurs)
C = [1, 10, 1, 100, 10, 1, -100, -10, -1]

def solve():
    # Calcule un truc avec C et N, renvoie 1 si égal à 0, sinon 0
    total = 0
    for i in range(9):
        total += C[i] * N[i]
    return 1 if total == 0 else 0

def dfs(index, left):
    # Si y'a plus rien à placer, on vérifie la condition
    if left == 0:
        return solve()
    
    if N[index] != -1:
        # Case déjà fixée, on passe à la suivante
        return dfs(index + 1, left)
    
    count = 0
    # On essaie toutes les possibilités pour cette position
    for _ in range(left):
        val = deq.popleft()
        N[index] = val
        count += dfs(index + 1, left - 1)
        deq.append(val)  # remets à la fin pour pas perdre le chiffre

    N[index] = -1  # reset, pas super propre, mais bon
    return count

print(dfs(0, len(deq)))