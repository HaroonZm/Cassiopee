lst = []
for i in range(6):
    s = input().split()
    s_set = set()
    for num in s:
        s_set.add(int(num))
    lst.append(s_set)

rec = []
while len(lst) > 0:
    x = lst[0]
    count = lst.count(x)
    if count % 2 == 1:
        print("no")
        break
    rec.append((count, x))
    for j in range(count):
        lst.remove(x)
else:
    if len(rec) == 1:
        if len(rec[0][1]) == 1:
            print("yes")
        else:
            print("no")
    elif len(rec) == 2:
        rec.sort()
        if rec[0][1].intersection(rec[1][1]) == rec[0][1]:
            print("yes")
        else:
            print("no")
    elif len(rec) == 3:
        if len(rec[0][1]) == 2 and len(rec[1][1]) == 2 and len(rec[2][1]) == 2:
            union_set = rec[0][1].union(rec[1][1])
            if rec[2][1].intersection(union_set) == rec[2][1]:
                print("yes")
            else:
                print("no")
        else:
            print("no")