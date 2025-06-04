import sys
sys.setrecursionlimit(100000)

def main():
    # Fonction qui calcule le nombre minimum de mouvements pour déplacer les disques
    def toC(A, B, C):
        if not (A or B):
            return 0
        if C & 1:
            return toC(A >> 1, B >> 1, C >> 1)
        if B & 1:
            return toC(C >> 1, B >> 1, A >> 1) + toC((A | B | C) >> 1, 0, 0) + 1
        if A & 1:
            return toC(A >> 1, B >> 1, C >> 1) + 2 * toC((A | B | C) >> 1, 0, 0) + 2

    while True:
        # Lire n et m
        data = input().split()
        n = int(data[0])
        m = int(data[1])
        cups = [0, 0, 0]
        if n == 0:
            break
        # Lire chaque pile
        for i in range(3):
            a = list(map(int, input().split()))
            for s in a[1:]:
                cups[i] |= 1 << (s - 1)
        normal = toC(cups[0], cups[1], cups[2])
        reversed_order = toC(cups[2], cups[1], cups[0])
        min_moves = min(normal, reversed_order)
        if min_moves <= m:
            print(min_moves)
        else:
            print(-1)

if __name__ == "__main__":
    main()