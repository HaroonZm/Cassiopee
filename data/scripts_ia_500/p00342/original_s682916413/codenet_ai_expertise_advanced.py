from sys import stdin

n, *data = map(int, stdin.read().split())
data.sort()

# Recherche de la plus petite différence dans une sous-liste
def min_diff(arr):
    pairs = zip(arr, arr[1:])
    return min(((b - a, a, b) for a, b in pairs), key=lambda x: x[0])

A, B, *rest = data
C, D = min_diff(data[2:])[1:]
ans_1 = (rest[-1] + rest[-2]) / (C - D)

C, D = min_diff(data)[1:]
tmp = data.copy()
tmp.remove(C)
tmp.remove(D)
A, B = tmp[-2], tmp[-1]
ans_2 = (A + B) / (C - D)

print(max(ans_1, ans_2))