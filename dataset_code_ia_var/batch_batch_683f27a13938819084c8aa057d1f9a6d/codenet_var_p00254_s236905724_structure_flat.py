from functools import reduce
while True:
    n = input()
    if n == "0000":
        break
    if len(n) < 4:
        n = "0"*(4-len(n)) + n
    same = True
    for ch in n:
        if ch != n[0]:
            same = False
            break
    if same:
        print("NA")
    else:
        cnt = 0
        while n != "6174":
            nlist = list(n)
            nlist.sort()
            s = ''.join(nlist)
            nlist.sort(reverse=True)
            l = ''.join(nlist)
            n = str(int(l) - int(s))
            if len(n) < 4:
                n = "0"*(4-len(n)) + n
            cnt += 1
        print(cnt)