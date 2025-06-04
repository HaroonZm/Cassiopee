from sys import stdin
from itertools import islice

def compute_grundy(N, M):
    grundy = [{0}, {1}]
    m = M
    while m // 2 >= N:
        idx = ((m + 1) // 2) % 2
        l = grundy[idx]
        m, r = divmod(m, 2)
        rest = {0, 1, 2} - grundy[0] - l if r == 0 else {0, 1, 2} - grundy[1] - l
        g = {min(rest)}
        if r == 0:
            grundy = [g, {0, 1, 2} - grundy[0] - g]
        else:
            grundy = [{min({0, 1, 2} - grundy[1] - l)}, {0, 1, 2} - grundy[1] - grundy[0]]
    return (grundy[1] if (m - N) % 2 else grundy[0]).pop()

def main():
    it = iter(stdin.read().split())
    K = int(next(it))
    ans = 0
    for _ in range(K):
        N, M = int(next(it)), int(next(it))
        ans ^= compute_grundy(N, M)
    print("tubuann" if ans == 0 else "mo3tthi")

main()