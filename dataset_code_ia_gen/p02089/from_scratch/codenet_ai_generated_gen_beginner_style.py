import sys

def trunc_towards_zero(value):
    if value >= 0:
        return value // 1
    else:
        return -((-value) // 1)

def main():
    input = sys.stdin.readline
    N, Q, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    for _ in range(Q):
        q, x, s, t = map(int, input().split())
        if q == 1:
            # For elements >= x
            for i in range(N):
                if A[i] >= x:
                    A[i] = t * (A[i] + s)
        else:
            # For elements <= x
            for i in range(N):
                if A[i] <= x:
                    val = (A[i] - s) / t
                    if val >= 0:
                        A[i] = int(val // 1)
                    else:
                        A[i] = -int((-val) // 1)
    
    count = 0
    for v in A:
        if L <= v <= R:
            count += 1
    print(count)

if __name__ == "__main__":
    main()