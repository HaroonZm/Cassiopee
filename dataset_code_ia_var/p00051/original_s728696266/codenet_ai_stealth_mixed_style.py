n = int(input())
i = 0
while i < n:
    A, B = '', ''
    s = input()
    stuff = list(s)
    asc = sorted(stuff)
    desc = list(asc)
    desc.reverse()
    for idx in range(8):
        A += desc[idx]
        B = B + asc[idx]
    print(int(A) - int(B))
    i += 1