tbl = dict(zip([1,2,3,4], (6e3,4e3,3e3,2e3)))

exec('for _ in[0]*4:\n l=input().split()\n print(tbl[int(l[0])]*int(l[1]))')