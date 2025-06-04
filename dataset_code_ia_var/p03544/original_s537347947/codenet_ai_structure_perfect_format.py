N = int(input())
lucas = [0 for i in range(N + 1)]

def luca(a):
    if a == 0:
        return 2
    elif a == 1:
        return 1
    else:
        if lucas[a] != 0:
            return lucas[a]
        else:
            lucas[a] = luca(a - 1) + luca(a - 2)
            return lucas[a]

print(luca(N))