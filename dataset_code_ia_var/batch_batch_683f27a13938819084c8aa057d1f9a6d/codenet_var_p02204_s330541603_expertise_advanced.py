from sys import stdin
from itertools import islice

def main():
    M_N_line = next(stdin)
    M, N = map(int, M_N_line.split())
    A = list(map(int, next(stdin).split()))
    if M >= 3:
        ans = sum(
            1 for k, (prev, curr) in enumerate(zip(A, islice(A,1,None)))
            if prev == curr
        )
        print(ans)
    else:
        def count_changes(start):
            now = start
            cnt = int(A[0] != start)
            for v in islice(A, 1, None):
                if v == now:
                    now = 3 - now
                    cnt += 1
                else:
                    now = v
            return cnt
        print(min(count_changes(A[0]), count_changes(3 - A[0])))

if __name__ == "__main__":
    main()