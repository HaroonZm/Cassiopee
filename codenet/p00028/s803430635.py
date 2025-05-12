a={}
maxnum = 1
while True:
    try:
        ai = int(input())
        if ai not in a:
            a[ai] = 1
        else:
            a[ai] += 1
            if maxnum < a[ai]:
                maxnum = a[ai]
    except:
        break
b = sorted(a.items())
for key, value in b:
    if maxnum==value:
        print(key)