from functools import reduce
from itertools import accumulate, chain, repeat, takewhile, starmap

clst = [10, 50, 100, 500]

def sgn(t):
    return next(filter(lambda x: clst[x] == t, range(4)))

def cnt(l1, l2, N):
    idx = sgn(l1[N])
    l2[idx] = l2[idx] + 1

def shiharai(bill, purse):
    coins = list(chain.from_iterable(repeat(clst[i], purse[i]) for i in range(4)))
    accums = list(accumulate(coins))
    pay = [0, 0, 0, 0]
    B = bill
    while B > 0:
        i = next((ix for ix, v in enumerate(accums) if v >= B), None)
        if accums[i] == B:
            list(starmap(lambda j, _: cnt(coins, pay, j), enumerate(repeat(None, i+1))))
            B -= sum(coins[:i+1])
        else:
            cnt(coins, pay, i)
            B -= coins[i]
    purse = list(map(lambda x, y: x - y, purse, pay))
    purse[0] -= B // 10
    return purse

def exchng(purse, n, r):
    while purse[n] >= r:
        purse[n] -= r
        purse[n+1] += 1

def ryogae(purse):
    list(starmap(lambda n, r: exchng(purse, n, r), zip([0, 1, 2], [5, 2, 5])))
    return purse

L = 0
while True:
    bill = int(input().strip())
    if bill == 0:
        break
    if L:
        print()
    lst = list(map(int, input().strip().split()))
    purse = list(map(int, lst))
    purse = shiharai(bill, purse)
    purse = ryogae(purse)
    shouldpay = list(map(lambda x, y: max(x - y, 0), lst, purse))
    list(starmap(lambda i, x: print(clst[i], x) if x else None,
        enumerate(shouldpay)))
    L += 1