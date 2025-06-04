ng = 0
class Pr:
    @staticmethod
    def is_prime(x):
        if x == 1: return True
        j = 3
        while j <= x // j:
            if not x % j:
                return False
            j = j + 2
        return True

try:
    n = int(input())
    for _ in [*range(n)]:
        val = input()
        p = (lambda v: 2 * int(v) + 1)(val)
        ng += Pr.is_prime(p)
finally:
    print(ng)