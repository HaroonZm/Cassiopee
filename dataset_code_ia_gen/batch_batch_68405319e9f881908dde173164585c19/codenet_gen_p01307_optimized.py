def solve():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    from functools import lru_cache

    n = int(input())
    for _ in range(n):
        s = input().strip()

        @lru_cache(None)
        def can_win(number):
            if len(number) == 1:
                return False
            digits = list(map(int, number))
            length = len(digits)
            # essayer toutes les paires i, i+1
            for i in range(length-1):
                new_digits = digits[:i] + [digits[i]+digits[i+1]] + digits[i+2:]
                new_number = tuple(new_digits)
                # si l'adversaire ne peut pas gagner à partir de new_number alors on gagne
                if not can_win(new_number):
                    return True
            return False

        result = can_win(tuple(map(int, s)))
        print("Fabre wins." if result else "Audrey wins.")