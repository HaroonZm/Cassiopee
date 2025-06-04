import itertools

n = int(input())

k, *list_b = map(int, input().split())

list_d = []

for k in range(len(list_b) + 1):
    for tuple_e in itertools.combinations(list_b, k):
        d = 0
        for bit in tuple_e:
            d += 2 ** bit
        list_d.append((d, tuple_e))

for d, tuple_e in sorted(list_d):
    if tuple_e:
        print(f"{d}: ", end="")
        print(*tuple_e)
    else:
        print(f"{d}:")