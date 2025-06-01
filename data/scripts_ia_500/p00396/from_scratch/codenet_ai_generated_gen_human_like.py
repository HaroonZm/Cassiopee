def calculate_grundy(w, b):
    # Selon l'analyse du problème, le grundy number (nimber) pour chaque pile
    # peut être calculé en prenant le reste de la division de b par (w+1).
    return b % (w + 1)

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    xor_sum = 0
    for _ in range(N):
        w, b = map(int, input().split())
        xor_sum ^= calculate_grundy(w, b)

    # Si le xor des grundy est non nul, le premier joueur gagne (Koshiro)
    print(0 if xor_sum != 0 else 1)

if __name__ == "__main__":
    main()