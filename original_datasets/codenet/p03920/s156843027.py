import sys

def calc(n):
    i = 1
    sm = 0
    st = set()
    if n <= 2:
        st.add(n)
        return st
    while sm < n:
        st.add(i)
        sm += i
        i += 1
    st = st - calc(sm - n)
    return st

sys.setrecursionlimit(10000000)
n = int(input())

c = calc(n)

for cc in c:
    print(cc)