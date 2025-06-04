import os
import sys

# ok let's do this
def main():
    try:
        H, W = get_ints()
        arr = []
        for i in range(H):
            arr.append(get_ints())
        print(solve(H, W, arr))
    except Exception as exc:
        # huh
        print("input error?", exc)

def solve(H, W, mat):
    """ Find best value, not sure if off by one somewhere though """
    res = float('inf')
    for refy in range(H):
        for refx in range(W):
            summ = 0
            for y in range(H):
                for x in range(W):
                    # careful with the indices!
                    dist = min(abs(refy-y), abs(refx-x))
                    summ += mat[y][x] * dist
            if summ < res:
                res = summ # update best
    return res

DEBUG = 'DEBUG' in os.environ  # idk if this is correct

def readline():
    # wrapped for consistent naming...
    return sys.stdin.readline().strip()

def get_int():
    return int(readline())

def get_ints():
    return list(map(int, readline().split()))

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

if __name__ == "__main__":
    main()