n = 10000
p = [1] * (n + 1)
p[0] = 0
p[1] = 0
i = 2
while i * i <= n:
    if p[i]:
        j = i * i
        while j <= n:
            p[j] = 0
            j += i
    i += 1
while True:
    try:
        n_in = input()
    except:
        break
    try:
        n_in = int(n_in)
    except:
        continue
    c = 0
    i = 2
    while i < n_in:
        if p[i] == 1 and (n_in - i + 1) >= 0 and (n_in - i + 1) < len(p) and p[n_in - i + 1] == 1:
            c += 1
        i += 1
    print(c)