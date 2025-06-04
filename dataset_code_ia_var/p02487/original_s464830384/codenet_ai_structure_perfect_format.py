import sys
import math

def solve():
    a, b = map(int, raw_input().split())
    while [a, b] != [0, 0]:
        for i in range(a):
            out = ""
            for j in range(b):
                if i == 0 or i == a - 1:
                    out += "#"
                else:
                    if j == 0 or j == b - 1:
                        out += "#"
                    else:
                        out += "."
            print out
        print ""
        a, b = map(int, raw_input().split())

if __name__ == "__main__":
    solve()