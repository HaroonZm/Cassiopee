n = 10001
list1 = [True for _ in xrange(n + 1)]
i = 2
while i * i <= n:
    if list1[i]:
        j = i + i
        while j <= n:
            list1[j] = False
            j += i
    i += 1
list1[1] = False
del list1[0]
while True:
    try:
        n_input = int(raw_input())
    except EOFError:
        break
    l = list1[:n_input]
    r = l[::-1]
    ans = 0
    j_idx = 0
    while j_idx < len(l):
        j = l[j_idx]
        k = r[j_idx]
        if j and k:
            ans += 1
        j_idx += 1
    print ans