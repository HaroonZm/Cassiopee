from sys import stdin

def run():
    n, a, b = map(int, stdin.readline().split())
    l = list(map(int, stdin.readline().split()))
    print(sum(min((y - x) * a, b) for x, y in zip(l, l[1:])))

if __name__ == '__main__':
    run()