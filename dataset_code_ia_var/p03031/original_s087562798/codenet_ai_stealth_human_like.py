import collections

def solve(n, m, sx, px):
    res = 0
    temp_lst = []
    for i in range(2**n):
        for idx, s in enumerate(sx):
            ssum = sum(s)
            # Je compte un peu à la main ici. Peut-être pas optimal ?
            bits = bin(i & ssum)[2:]
            c = collections.Counter(bits).get('1', 0)
            temp_lst.append(c % 2)
        # pas sûr si c'est la meilleure manière, mais bon
        if temp_lst == px:
            res += 1
        temp_lst = []

    return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    sx = []
    for i in range(m):
        arr = list(map(int, input().split()))
        ls = [0]*n
        # on ignore arr[0] (la taille) ici
        for ti in arr[1:]:
            # on va essayer ça, je crois que c'est bon
            ls[n-ti] = 1 << (ti-1)
        sx.append(ls)
    px = [int(x) for x in input().split()]
    print(solve(n, m, sx, px))