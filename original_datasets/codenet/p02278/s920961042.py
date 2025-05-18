def solve(n, A):
    def cycles():
        V = [False] * n
        B = sorted(A)
        T = {B[i]: i for i in range(n)}
        C = []

        for i in range(n):
            if V[i]:
                continue
            cur = i
            cycle = []
            while not V[cur]:
                V[cur] = True
                cycle.append(cur)
                cur = T[A[cur]]
            C.append(cycle)

        return C

    ans = 0
    s = min(A)

    for cycle in cycles():
        S = sum([A[i] for i in cycle])
        m = min([A[i] for i in cycle])
        an = len(cycle)
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)

    return ans

def main():
    n = int(input())
    A = [int(x) for x in input().split()]

    print(solve(n, A))

main()