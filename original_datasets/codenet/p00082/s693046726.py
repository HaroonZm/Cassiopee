mgr = [4, 1, 4, 1, 2, 1, 2, 1]

while True:
    try:
        p = list(map(int, input().split(' ')))
        v = []
        for i in range(8):
            q = mgr[i:] + mgr[:i]
            sum_v = sum(p) - sum(p[j]-q[j] if p[j]-q[j] >= 0 else 0 for j in range(8))
            v.append(sum_v)
        if v.count(max(v)) > 1:
            mv = max(v)
            ans = []
            for i in range(8):
                if v[i] == mv:
                    ans.append(int("".join(map(str, mgr[i:] + mgr[:i]))))
            print(" ".join(list(str(min(ans)))))
        else:
            i = v.index(max(v))
            print(" ".join(map(str, mgr[i:] + mgr[:i])))
    except:
        break