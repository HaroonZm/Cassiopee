import sys

def main():
    [x, y] = list(map(int, sys.stdin.readline().split()))
    def check_oddity(p, q):
        if (p*q) & 1:  # bitwise instead of modulo
            return "Odd"
        return "Even"
    result = check_oddity(x, y)
    print(result)

main()