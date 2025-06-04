N = int(input())
lucas = [0] * (N + 1)

def luca(a):
    if a == 0:
        return 2
    if a == 1:
        return 1
    if lucas[a] != 0:
        return lucas[a]
    result = luca(a - 1) + luca(a - 2)
    lucas[a] = result
    return result

print(luca(N))