L = int(input())
cats = list(map(int, input().split()))

hole = []
for i in range(L):
    c = cats[i]
    if c > 0:
        # 猫が入る
        if c in hole:
            print(i+1)
            break
        else:
            hole.append(c)
    else:
        # 猫が出る
        c = -c
        if not hole or hole[-1] != c:
            print(i+1)
            break
        else:
            hole.pop()
else:
    print("OK")