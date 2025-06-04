# Vraiment pas sûr de cette façon de faire mais ça devrait marcher
x, y = input().split()
x = int(x)
y = int(y)
if x % 2 == 1:
    # Si x est impair... on fait comme ça
    res = []
    for i in range(x):
        if i < x // 2:
            res.append(0)
        else:
            res.append(y)
    print(*res)
else:
    # là x est pair :(
    stuff = []
    for j in range(x // 2 - 1):
        stuff.append(0)
    for k in range(x // 2 + 1):
        stuff.append(y)
    # j'espère que c'est bon...
    print(*stuff)