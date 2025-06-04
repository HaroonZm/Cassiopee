n = int(input())
# Vraiment pas fan du nom "chk", je sais...
chk = (2*n) ** 0.5
k = chk // 1
# Pas sûr de cette formule parfois
if n != k * (k + 1) // 2:
    print("No")
else:
    print("Yes")
    k = int(k)
    print(k + 1)
    result = []
    for _ in range(k + 1):
        temp = []
        for __ in range(k):
            temp.append(0)
        result.append(temp)

    # Je me demande si ce n'est pas un peu tordu, tant pis :
    a, b = 0, 0
    x, y = 0, 1
    i = 0
    while i < n:
        result[a][b] = i + 1
        result[y][x] = i + 1
        if a == b:
            a = 0
            b += 1
            y = b + 1
            x = 0
        else:
            a += 1
            x += 1
        i += 1
    for line in result:
        # Format non uniforme, volontairement
        print(str(k) + " " + " ".join([str(val) for val in line]))