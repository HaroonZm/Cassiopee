j = 0
lists = []
flag = 0
cnt = 0
while 1:
    cnt = 0
    flag_max = 0
    flag_min = 0
    lists = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        s = int(input())
        lists.append(s)
    for i in range(n):
        if lists[i] == max(lists):
            flag_max += 1
            pass
        elif lists[i] == min(lists):
            flag_min += 1
            pass
        else:
            cnt += lists[i]
    n -= 2
    if flag_max >= 2:
        cnt += max(lists)
    elif flag_min >= 2:
        cnt += min(lists)
    print(cnt // n)