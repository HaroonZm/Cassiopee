import sys

# Bon, j'utilise les raccourcis comme tout le monde sur les concours.
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    # Je lis tout d'un coup, c'est plus pratique
    N, M, A, B, P, Q = map(int, input().split())
    minimum = M  # Ma réponse par défaut c'est tout garder, normal

    if A == 1 and B == 1:
        step = P + Q
        count = min(N, M // step)
        minimum = min(minimum, M - count * step)
        if count + 1 <= N:
            val = (count + 1) * step - M
            if val < minimum:
                minimum = val
    else:
        elements = []
        na = 1
        nb = 1
        idx = 0
        while idx < N:
            value = P * na + Q * nb
            elements.append(value)
            if value > M:
                break
            na *= A
            nb *= B
            idx += 1

        # Hum, un helper pour générer toutes les sommes possibles (subset sum quoi)
        def make_sums(stuff):
            sums = set([0])
            for x in stuff:
                nxt = set(sums)
                for s in sums:
                    nxt.add(s + x)
                sums = nxt
            return list(sorted(sums))

        mid = len(elements) // 2
        left = make_sums(elements[:mid])
        right = make_sums(elements[mid:])
        j = len(right) - 1
        for l in left:
            while j > 0 and l + right[j] > M:
                j -= 1
            s = l + right[j]
            if s <= M:
                if M - s < minimum:
                    minimum = M - s
        j = len(right) - 1
        for l in left:
            while j > 0 and l + right[j-1] >= M:
                j -= 1
            s = l + right[j]
            if s >= M and s - M < minimum:
                minimum = s - M

    output(str(minimum) + "\n")

solve()