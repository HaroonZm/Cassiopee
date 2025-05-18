INF = 10**3

def reconstruction(o_ary, p_ary, i_ary, l, r):
    if l >= r:
        return

    ind = INF
    for i in i_ary[l:r]:
        tmp_ind = p_ary.index(i)
        if ind > tmp_ind:
            ind = tmp_ind
    c = p_ary[ind]
    m = i_ary.index(c)

    reconstruction(o_ary, p_ary, i_ary, l, m)
    reconstruction(o_ary, p_ary, i_ary, m + 1, r)
    o_ary.append(c)

n = int(input())
p_ary = [int(_) for _ in input().split()]
i_ary = [int(_) for _ in input().split()]
o_ary = []
reconstruction(o_ary, p_ary, i_ary, 0, n)
print(*o_ary)