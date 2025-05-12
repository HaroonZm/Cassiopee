n = int(input())
ls = []
for i in xrange(0, n):
    ls.append(int(input()))
sls = sorted(ls)
st = {j for i, j in enumerate(ls) if i % 2 == 1}
sst = {j for i, j in enumerate(sls) if i % 2 == 1}
print(len(st.difference(sst)))