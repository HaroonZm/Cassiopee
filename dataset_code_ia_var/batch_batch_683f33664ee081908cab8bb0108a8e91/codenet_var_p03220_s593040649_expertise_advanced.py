from sys import stdin
from operator import itemgetter

def main():
    n = int(stdin.readline())
    t, a = map(int, stdin.readline().split())
    h = list(map(int, stdin.readline().split()))
    temps = (t - 0.006 * hi for hi in h)
    ans, _ = min(enumerate(temps, 1), key=lambda ix: abs(a - ix[1]))
    print(ans)

if __name__ == '__main__':
    main()