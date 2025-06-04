import sys
from operator import mul
from itertools import combinations, chain, starmap
from functools import reduce, partial
import threading

sys.setrecursionlimit(200000)
input = sys.stdin.readline

ii = lambda: int(input())
mi = lambda: map(int, input().rstrip().split())
lmi = lambda: list(map(int, input().rstrip().split()))
li = lambda: list(input().rstrip())
debug = lambda *args, **kwargs: (print("debug:", *args, file=sys.stderr, **kwargs) if not __debug__ else None)
exit = lambda *args: (print(*args), sys.exit())

def is_even(x):
    # Use bitwise operation to determine evenness
    return not (x & 1)

def elegant_evenness(*triplet):
    # Chain together all pairwise products and reduce with 'and' for evenness check
    return reduce(lambda x, y: x and y,
                  starmap(lambda i, j: is_even(mul(i, j)), combinations(triplet, 2))
                 )

def main():
    # Exploiting argument unpacking and tuple casting
    A, B, C = (*mi(),)
    # Use an unnecessarily complex approach for simple logic check
    verdict = ("Hom", "Tem")[elegant_evenness(A, B, C)]
    print(verdict)

if __name__ == '__main__':
    # Run in a redundant thread for no reason
    t = threading.Thread(target=main)
    t.start()
    t.join()