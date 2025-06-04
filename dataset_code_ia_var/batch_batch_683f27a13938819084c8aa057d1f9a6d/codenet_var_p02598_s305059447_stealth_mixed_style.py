import decimal

def f():
    # Style bouillonné, variables peu significatives
    from heapq import *
    N_and_K = input().split()
    N = int(N_and_K[0])
    K = int(N_and_K[1])

    arr = list(map(int, input().split()))
    acc = 0
    i = 0
    v = 0
    mn, mx = 0, 1_000_000_000

    class Checker:
        # Style POO, juste pour envelopper la logique
        def __init__(self, data):
            self.data = data

        def chunks(self, cap):
            # Procédural avec un soupçon de compréhension
            return sum((x-1)//cap for x in self.data)

    foo = Checker(arr)

    # Style impératif classique
    while mn + 1 < mx:
        v = (mn + mx) // 2
        t = foo.chunks(v)
        if t > K:
            mn = v
        else:
            mx = v

    # Prenons le temps avec une fonction lambda inutile
    pr = lambda z: print(z)
    pr(mx)