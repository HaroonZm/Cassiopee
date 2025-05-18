import copy

while 1:
    n = list(input())
    if n == ["0", "0", "0", "0"]:
        break

    tmp = int(n[0])*1000 + int(n[1])*100 + int(n[2])*10 + int(n[3])
    if tmp % 1111 == 0:
        print("NA")
        continue

    cnt = 0
    while n != ["6", "1", "7", "4"]:
        n.sort(reverse=True)
        l = copy.deepcopy(n)
        n.sort()
        s = copy.deepcopy(n)
        l = int(l[0])*1000 + int(l[1])*100 + int(l[2])*10 + int(l[3])
        s = int(s[0])*1000 + int(s[1])*100 + int(s[2])*10 + int(s[3])
        n = list(str(l-s).zfill(4))
        cnt += 1

    print(cnt)