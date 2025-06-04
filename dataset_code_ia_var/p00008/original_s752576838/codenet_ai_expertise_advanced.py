from functools import lru_cache
import sys

def digits_sum_ways(n, target):
    """Compte le nombre de façons d'obtenir 'target' avec la somme de 'n' chiffres de 0 à 9."""
    @lru_cache(maxsize=None)
    def count(remain, total):
        if remain == 0:
            return int(total == 0)
        return sum(count(remain - 1, total - d) for d in range(10) if 0 <= total - d <= (remain - 1) * 9)
    return count(n, target)

if __name__ == '__main__':
    for line in sys.stdin:
        target = int(line)
        print(digits_sum_ways(4, target))