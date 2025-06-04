import sys

def get_input():
    return list(map(int, input().split()))

def main():
    [A, B, C] = get_input()
    res = None
    arrived = 0
    def check(t): return t % 60

    t = 0
    # boucle à la C
    while True:
        mod = check(t)
        if mod <= C and C <= (mod + A):
            arrived = 1
            break
        t += (A + B)
        if check(t) == 0:
            break

    # style ternaire
    print((C + 60 * (t // 60)) if arrived else -1)

main()