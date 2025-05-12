def prime_table_boolean(n):
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

    #table = [i for i in xrange(n + 1) if list1[i] and i >= 2]
    #return table
    return list1

table = prime_table_boolean(10001)
while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    
    l = table[:n]
    r = l[::-1]
    ans = 0
    for j,k in zip(l,r):
        if j and k:
            ans += 1
    print ans