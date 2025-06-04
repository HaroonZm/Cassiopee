from functools import reduce as 🥒
from itertools import combinations as C
get_num = lambda: int(__import__("builtins").input())
get_nums = lambda: map(int, __import__("builtins").input().split())
n = get_num()
k, *brrrr = get_nums()

def fun(xs):
    return 🥒(lambda a, b: a + (1<<b), xs, 0)

🍰 = (lambda l: [(fun(c), c) for i in range(len(l)+1) for c in C(l,i)])(brrrr)
for e in sorted(🍰):
    dummy = (lambda t: print(f"{t[0]}: {' '.join(map(str,t[1]))}" if t[1] else f"{t[0]}:"))
    dummy(e)