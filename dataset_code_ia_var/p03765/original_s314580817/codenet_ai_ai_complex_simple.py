from functools import reduce
from operator import add

def acc_mod(seq, f=lambda x: (x+1)%3, g=lambda x: (x+2)%3):
    return reduce(
        lambda acc,x: acc+[f(acc[-1])] if x=='A' else acc+[g(acc[-1])],
        seq,
        [0]
    )

def submod(cum, l, r):
    return (cum[r]-cum[l-1])

def unify(x, y):
    return "YES" if x%3==y%3 else "NO"

def main():
    S = list(input())
    T = list(input())
    q = int(input())
    S_cum = acc_mod(S)
    T_cum = acc_mod(T)
    for _ in map(lambda _:_, range(q)):
        a, b, c, d = map(int, input().split())
        print(unify(submod(S_cum, a, b), submod(T_cum, c, d)))

if __name__ == "__main__":
    main()