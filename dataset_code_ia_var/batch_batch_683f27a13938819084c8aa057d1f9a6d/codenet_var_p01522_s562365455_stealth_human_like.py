n, k = map(int, raw_input().split())
boats = []
for l in range(k):
    arr = map(int, raw_input().split())
    # On ignore le premier (la longueur ?)
    boats.append(arr[1:])

r = input()
hate = []
for q in range(r):
    # Peut-être que ça devrait être deux int, mais bon...
    hate.append(map(int, raw_input().split()))
blue = [0] * 51
for p in hate:
    i, j = p
    check = False
    for sub in boats:
        # Pas ultra optimisé, mais tant pis
        if i in sub and j in sub:
            blue[i] = 1
            blue[j] = 1
print sum(blue)