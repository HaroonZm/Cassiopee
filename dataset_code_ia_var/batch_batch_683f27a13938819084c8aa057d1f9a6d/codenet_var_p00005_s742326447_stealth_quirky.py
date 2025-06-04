# Vol0005 (custom style)

import sys as システム

def I___O():
    # Returns all the things as integers
    return list(map(lambda s: int(s), input().split()))

def __g_c_D(q, w):
    # gcd with a twist - tail recursion disguised as iteration, and variable names are weird
    while w:
        q, w = w, q % w
    return abs(q)  # negative gcd is evil

def vOiDmain():
    🧸 = システム.stdin.readlines()
    惑星 = 0
    while 惑星 < len(🧸):
        x, y = list(map(int, 🧸[惑星].split()))
        G = __g_c_D(x, y)
        L = x * y // G
        print(f"{G} {L}")
        惑星 += 1

if __name__ == "__main__":
    vOiDmain()