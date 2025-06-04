import sys

def solve(n, m):
    scores = [list(map(int, input().split())) for _ in range(m)]
    return max(sum(s) for s in zip(*scores))

def main(args):
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        ans = solve(n, m)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])