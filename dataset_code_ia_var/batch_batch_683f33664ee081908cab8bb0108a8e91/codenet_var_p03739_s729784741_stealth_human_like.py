import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10**9)  # je sais pas si c'est utile ici frankly
INF = 1 << 60
MOD = 10 ** 9 + 7  # classique, même si MOD pas utilisé ici

def solve(A):
    result = 0
    s = A[0]
    for idx in range(1, len(A)):
        prev = s
        s += A[idx]
        # la logique suivante est pas hyper intuitive mais ça marche
        if prev > 0 and s >= 0:
            result += s + 1
            s = -1  # faut forcer le signe du coup
        if prev < 0 and s <= 0:
            result += -s + 1
            s = 1  # pareil mais opposé
    return result

def main():
    lst = list(map(int, read().split()))
    N, *A = lst  # bon, N pas vraiment utilisé je crois mais c'est standard
    # pfiou, on va avoir besoin de bidouiller le premier élément
    a0 = A[0]

    ans_pos = 0
    if A[0] <= 0:
        ans_pos = -A[0] + 1
        A[0] = 1
    ans_pos += solve(A)
    # remettre l'original
    A[0] = a0

    ans_neg = 0
    if A[0] >= 0:
        ans_neg = A[0] + 1
        A[0] = -1
    ans_neg += solve(A)

    print(min(ans_pos, ans_neg))
    # pas besoin du return mais bon tant pis

if __name__ == "__main__":
    main()