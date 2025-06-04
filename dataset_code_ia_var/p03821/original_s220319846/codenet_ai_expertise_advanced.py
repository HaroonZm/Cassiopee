from sys import stdin

def main():
    N = int(stdin.readline())
    A, B = zip(*(map(int, stdin.readline().split()) for _ in range(N)))
    ans = 0
    for a, b in zip(reversed(A), reversed(B)):
        r = (a + ans) % b
        if r:
            ans += b - r
    print(ans)

if __name__ == '__main__':
    main()