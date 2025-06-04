import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        A_B_P = line.strip().split()
        if len(A_B_P) != 3:
            continue
        A, B, P = map(int, A_B_P)
        if A == 0 and B == 0 and P == 0:
            break
        N = B - A + 1
        data = [0] * (N + 2)

        def get(k):
            s = 0
            while k > 0:
                s += data[k]
                k -= (k & -k)
            return s % P

        V = []
        for i in range(A, B+1):
            V.append(i)
        V = sorted(V, key=lambda x: str(x))

        for v in V:
            k = v + 1 - A
            x = get(k) + 1
            i = k
            while i <= N:
                data[i] += x
                i += (i & -i)

        result = get(N) % P
        print(result)

main()