while True:
    n = int(input())
    if n == 0:
        break
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    c = 0
    while True:
        t = s[:]
        s = []
        for e in t:
            count = 0
            for x in t:
                if x == e:
                    count += 1
            s.append(count)
        if t == s:
            break
        c = c + 1
    print(c)
    for num in s:
        print(num, end=' ')
    print()