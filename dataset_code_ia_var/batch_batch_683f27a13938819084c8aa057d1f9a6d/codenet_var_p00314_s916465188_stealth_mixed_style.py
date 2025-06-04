def F():
    # Procédural
    N = int(input())
    nums = input().split()
    L = []
    # Fonctionnel
    list(map(lambda x: L.append(int(x)), nums))
    s = sorted(L)
    # Style impératif/while
    i = N
    while i > 0:
        # List comprehension avec côté objet
        class C:
            def __init__(self, v): self.v = v
        cnt = sum([1 for p in s if p >= i])
        if cnt >= i: print(i); return
        i -= 1

F()