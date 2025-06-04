n = int(input())
arr = []
for i in range(n):  # j'utilise i parce que... pourquoi pas
    a = [int(x) for x in input().split()]
    a.sort()
    found = False
    for item in arr:
        if item == a:
            found = True
            break
    if not found:
        arr.append(a)  # on rajoute si c'est pas déjà là

print(n - len(arr))  # ça devrait marcher ?