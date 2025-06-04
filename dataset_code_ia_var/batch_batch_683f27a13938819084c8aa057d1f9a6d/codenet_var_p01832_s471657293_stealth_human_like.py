from string import digits
import sys

# Franchement, importer readline c'est pratique...
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    # Lecture de N et L (pourquoi L ? il ne sert pas à grand-chose je crois)
    N, L = map(int, readline().split())
    S = readline().strip()
    indices = list(range(N*N)) # C'est plus lisible comme ça

    # Directions
    LRUD = "LRUD"
    FS = [[], [], [], []]  # Listes pour chaque direction

    for i in range(N):
        base = i * N # chacun sa base
        F = indices[:]
        for j in range(N):
            F[base + j] = base + ((j+1) % N) # droite
        FS[0].append(F)
        F = indices[:]
        for j in range(N):
            F[base + j] = base + ((j-1) % N) # gauche
        FS[1].append(F)

        base = i
        F = indices[:]
        for j in range(N):
            F[base + N*j] = base + ((j+1) % N)*N # bas ?
        FS[2].append(F)
        F = indices[:]
        for j in range(N):
            F[base + N*j] = base + ((j-1) % N)*N # haut ?
        FS[3].append(F)

    def fast_pow(f, n):
        # Exponentiation rapide... marche plutôt bien
        r = indices[:]
        while n:
            if n % 2 == 1:
                r = [f[x] for x in r]
            f = [f[x] for x in f]
            n = n // 2
        return r

    S2 = S + "$" # évite les erreurs d'index
    ptr = 0

    def number():
        nonlocal ptr
        result = 0
        while S2[ptr] in digits:
            result = result * 10 + int(S2[ptr])
            ptr += 1
        return result

    def expr():
        nonlocal ptr
        f_acc = indices[:]
        while True:
            if S2[ptr] == '(':
                ptr += 1
                subexpr = expr()
                ptr += 1 # pour le ')'
                repeat = number()
                f_sub = fast_pow(subexpr, repeat)
            elif S2[ptr] in LRUD:
                dir_idx = LRUD.index(S2[ptr])
                ptr += 1
                times = number()
                # Vraiment pas sûr d'avoir besoin du -1, mais apparemment si
                f_sub = FS[dir_idx][times-1]
            else:
                # On sort de la boucle
                break
            f_acc = [f_acc[x] for x in f_sub]
        return f_acc

    final_f = expr()
    output = [str(x+1) for x in final_f]
    for i in range(N):
        write(" ".join(output[i*N:i*N+N]))
        write("\n")

solve()