def main():
    n,m = map(int,input().split())
    if n*m == 0: return False
    a = list(map(int, input().split()))
    w = list(map(int,input().split()))
    d = {0:1}
    for i in w:
        new_d = dict(d)
        for j in d.keys():
            new_d[j+i] = 1
            new_d[abs(j-i)] = 1
        new_d[i] = 1
        d = dict(new_d)
    nokori = []
    for i in a:
        if i in d.keys():
            pass
        else:
            nokori += [i]
    # print(nokori)
    nokorimono = len(nokori)
    if nokorimono == 0:
        print(0)
        return True
    ans_d = {}
    for i in nokori:
        new_d = {}
        for j in d.keys():
            new_d[abs(i-j)] = 1
            new_d[i+j] = 1
        for j in new_d.keys():
            if j in ans_d:
                ans_d[j] = ans_d[j] + 1
            else:
                ans_d[j] = 1
    ans = 10**12
    for i in ans_d.keys():
        if ans_d[i] == nokorimono:
            ans = min(ans, i)
    if ans == 10**12:
        ans = -1
    print(ans)
    return True

while main():
    pass