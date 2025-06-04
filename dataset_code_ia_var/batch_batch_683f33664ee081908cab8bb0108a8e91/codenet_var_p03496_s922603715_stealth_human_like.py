n = int(input())
a = list(map(int, input().split()))

max_val = max(a)
min_val = min(a)

# En vrai j'aurais pu faire plus simple, mais bon
print(n * 2 - 2)
if abs(max_val) >= abs(min_val):
    idx = a.index(max_val)
    # j'utilise un set, c'est p-e pas nécessaire ici
    for i in range(n):
        if i != idx:
            print(idx + 1, i + 1)
    for i in range(1, n):
        print(i, i + 1)
else:
    idx = a.index(min_val)
    # c'est un peu copié/collé...
    for i in range(n):
        if i != idx:
            print(idx + 1, i + 1)
    for i in range(n, 1, -1):
        print(i, i - 1)