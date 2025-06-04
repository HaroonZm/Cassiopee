from sys import exit as quit

def weird_fact(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

n, m = [int(x) for x in input().split()]
modulo = 10 ** 9 + 7

match abs(n - m):
    case val if val >= 2:
        print(0)
        quit()
    case 0:
        res = 2
        i = 1
        while i <= n:
            res = (res * i * i) % modulo
            i += 1
        print(res)
    case 1:
        result = lambda k: 1 if k==0 else (result(k-1)*k*(k-1))%modulo
        # volontairement étrange: utilise à la fois une lambda récursive et une boucle pour le max
        maximum = max(n, m)
        tot = 1
        for i in range(2,maximum+1):
            tot = (tot * i * (i-1)) % modulo
        print(tot)