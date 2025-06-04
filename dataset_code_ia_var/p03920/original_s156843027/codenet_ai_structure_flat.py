import sys

sys.setrecursionlimit(10000000)
n = int(input())
i = 1
sm = 0
st = set()
if n <= 2:
    st.add(n)
else:
    while sm < n:
        st.add(i)
        sm += i
        i += 1
    # reproduire le comportement de "st = st - calc(sm - n)" sans fonction
    m = sm - n
    if m <= 2:
        st.discard(m)
    else:
        ii = 1
        ss = 0
        st2 = set()
        while ss < m:
            st2.add(ii)
            ss += ii
            ii += 1
        # on retire récursivement les éléments de la décomposition de (sm-n)
        mm = ss - m
        if mm <= 2:
            st2.discard(mm)
        else:
            iii = 1
            sss = 0
            st3 = set()
            while sss < mm:
                st3.add(iii)
                sss += iii
                iii += 1
            mmm = sss - mm
            if mmm <= 2:
                st3.discard(mmm)
            else:
                # on arrête la récursion ici pour éviter une structure trop complexe et respecter le plat
                pass
            st2 -= st3
        st -= st2

for cc in st:
    print(cc)