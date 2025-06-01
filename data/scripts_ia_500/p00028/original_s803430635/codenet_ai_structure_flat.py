a = {}
maxnum = 1
while True:
    try:
        ai = int(input())
        if ai in a:
            a[ai] += 1
            if a[ai] > maxnum:
                maxnum = a[ai]
        else:
            a[ai] = 1
    except:
        break
b = sorted(a.items())
for key, value in b:
    if value == maxnum:
        print(key)