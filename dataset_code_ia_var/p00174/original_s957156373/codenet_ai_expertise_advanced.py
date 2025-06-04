from itertools import islice, count
from sys import stdin

def calc(S):
    p = S.count('A', 1)
    q = len(S) - 1 - p
    return p, q

def check(p, q):
    return (q < 10 and p == 11) or (q >= 10 and p - q == 2)

def update_score(S, p, q):
    return (p + 1, q) if S[0] == 'A' else (p, q + 1)

def main():
    lines = iter(stdin.readline, '')
    while True:
        S1 = next(lines).rstrip()
        if S1 == '0': break
        S2 = next(lines).rstrip()
        S3 = next(lines).rstrip()

        p1, q1 = calc(S1)
        print(*update_score(S2, p1, q1))

        p2, q2 = calc(S2)
        print(*update_score(S3, p2, q2))

        p3, q3 = calc(S3)
        next_score = (p3 + 1, q3) if check(p3 + 1, q3) else (p3, q3 + 1)
        print(*next_score)

if __name__ == "__main__":
    main()