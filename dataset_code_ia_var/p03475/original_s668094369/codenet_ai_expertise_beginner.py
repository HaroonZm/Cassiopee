import sys

def main():
    n = int(input())
    C = []
    S = []
    F = []
    for _ in range(n-1):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)
    for start in range(n-1):
        time = S[start]
        for i in range(start, n-1):
            if time < S[i]:
                time = S[i]
            while time % F[i] != 0:
                time += 1
            time += C[i]
        print(time)
    print(0)

if __name__ == '__main__':
    main()