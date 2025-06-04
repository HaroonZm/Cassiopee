import sys
from functools import partial

readline = sys.stdin.readline
write = sys.stdout.write
flush = sys.stdout.flush

query = lambda n: (write(f"? {n}\n"), flush(), readline().strip() == 'Y')[2]
answer = lambda n: (write(f"! {n}\n"), flush())

def find_digits():
    """Détermine le nombre de chiffres requis via requêtes binaires optimisées."""
    for d in range(10):
        if not query(10**d):
            return d
    # Nombre est une puissance de 10, on le traite à part
    for d in range(10):
        if query(10**d + 1):
            answer(10**d)
            sys.exit(0)

def check(ans_digits, pos, nb_digits):
    n = int(''.join(map(str, ans_digits)))
    # Pour le dernier chiffre, tester s'il faut ajouter un zéro de plus pour détecter la fin
    return not query(n * 10) if pos == nb_digits - 1 else query(n)

def main():
    nb_digits = find_digits()
    ans_digits = [0] * nb_digits
    for i in range(nb_digits):
        left, right = (-1, 10) if i > 0 else (-1, 10)
        while left + 1 < right:
            mid = (left + right) // 2
            ans_digits[i] = mid
            if check(ans_digits, i, nb_digits):
                left = mid
            else:
                right = mid
        ans_digits[i] = left + 1 if i == nb_digits - 1 else left
    answer(int(''.join(map(str, ans_digits))))

main()