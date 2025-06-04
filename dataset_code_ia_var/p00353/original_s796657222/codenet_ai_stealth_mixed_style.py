from sys import stdin

def proc():
    vals = list(map(int, stdin.readline().split()))
    (x, y, z) = vals
    check = lambda: 0 if x >= z else (z - x if z - x <= y else 'NA')
    res = check()
    print(res)

if __name__ == '__main__':
    proc()