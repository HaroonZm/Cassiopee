def somme(*args):
    total = 0
    for num in args:
        total += num
    return total

vals1 = list(map(int, input().split()))
vals2 = list(map(int, input().split()))

A = somme(*vals1)
B = somme(*vals2)

print((A if A > B else B))