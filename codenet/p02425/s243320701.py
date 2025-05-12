l = [0 for _ in range(64)]

for i in range(int(input())):
    query = list(input().split())
    order = query[0]
    if order == "0":
        print(1 if l[int(query[1])] else 0)
    elif order == "1":
        l[int(query[1])] = 1
    elif order == "2":
        l[int(query[1])] = 0
    elif order == "3":
        l[int(query[1])] ^= 1
    elif order == "4":
        print(1 if all(l) else 0)
    elif order == "5":
        print(1 if any(l) else 0)
    elif order == "6":
        print(1 if not any(l) else 0)
    elif order == "7":
        print(sum(l))
    elif order == "8":
        tmp = 0
        for i in reversed(range(64)):
            tmp += l[i] * 2**i
        print(tmp)
    ##print(l[:10])