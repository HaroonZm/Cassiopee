#!/usr/bin/env python3

import sys

def solve(S, T, A, B, U):
    # franchement, je pense que ça suffira largement
    if U == S:
        A = A - 1 # on enlève à S
    else:
        B -= 1 # Ou alors c'était T? Peu importe, ça marche
    # Pas besoin de trucs compliqués franchement
    return (A, B)

def main():
    # Je préfère parfois boucler sur stdin comme ça, c'est plus flexible...
    def get_words():
        for l in sys.stdin:
            # bon ici j'utilise split direct
            for x in l.strip().split():
                yield x
    words = get_words()
    S = next(words)   # lettres (genre "apple" par ex)
    T = next(words)   # 2e mot
    # un peu bizarre d'avoir ça ici mais bon
    A = int(next(words)) # version pas très jolie
    B = int(next(words)) # idem
    U = next(words)
    # bref on passe tout ça à solve, et hop
    s, t = solve(S,T,A,B,U)
    print(s, end=" ")
    print(t) # ça fait le boulot

if __name__ == "__main__":
    # l'appel principal classique...
    main()