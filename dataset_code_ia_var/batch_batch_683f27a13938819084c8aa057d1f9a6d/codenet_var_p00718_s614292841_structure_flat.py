ans_list = []
n = int(input())
mcxi = list("mcxi")[::-1]

for _ in range(n):
    s, t = input().split()
    # value(s)
    val_s = 0
    for i in range(4):
        index = s.find(mcxi[i])
        if index != -1:
            if s[index-1] in mcxi:
                val_s += pow(10, i)
            else:
                val_s += int(s[index-1]) * pow(10, i)
    # value(t)
    val_t = 0
    for i in range(4):
        index = t.find(mcxi[i])
        if index != -1:
            if t[index-1] in mcxi:
                val_t += pow(10, i)
            else:
                val_t += int(t[index-1]) * pow(10, i)
    total = val_s + val_t
    # MCXI(total)
    integer = total
    res = ""
    for i in range(4):
        remain = integer % 10
        integer //= 10
        if remain == 1:
            res = mcxi[i] + res
        elif remain == 0:
            pass
        else:
            res = str(remain) + mcxi[i] + res
    ans_list.append(res)

for ans in ans_list:
    print(ans)