INF = 1000

def reconstruction(o_ary, p_ary, i_ary, l, r):
    if l >= r:
        return
    ind = INF
    for i in range(l, r):
        tmp = p_ary.index(i_ary[i])
        if tmp < ind:
            ind = tmp
    c = p_ary[ind]
    m = i_ary.index(c)
    reconstruction(o_ary, p_ary, i_ary, l, m)
    reconstruction(o_ary, p_ary, i_ary, m+1, r)
    o_ary.append(c)

n = int(input())
p_ary = list(map(int, input().split()))
i_ary = list(map(int, input().split()))
o_ary = []
reconstruction(o_ary, p_ary, i_ary, 0, n)
for x in o_ary:
    print(x, end=" ")