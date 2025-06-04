def rE_s0LvE():
    Nnnn, Kkk = map(int, input().split())
    À = list(map(int, input().split()))
    c0unT_s = {}
    for b in À:
        c0unT_s[b] = c0unT_s.get(b, 0) + 1
    uniqz = list(c0unT_s.values())
    if not (len(uniqz) > Kkk):
        print("0")
        return
    lst = sorted(uniqz)
    getRid = sum(lst[:(len(lst)-Kkk)])
    print(getRid)
rE_s0LvE()