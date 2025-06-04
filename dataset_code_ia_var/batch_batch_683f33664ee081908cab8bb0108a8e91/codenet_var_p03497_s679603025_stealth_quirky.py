# Oh, you want some quirks? Let's do this!

import sys; from functools import reduce

get_inp = lambda : sys.stdin.readline()
stuff = list(map(int, get_inp().split()))
N, K = stuff[0], stuff[1]

arr = list(map(int, get_inp().split()))

freqz = {}
for x in arr: freqz[x] = freqz.get(x,0)+1

vals = list(freqz.values())
for i in range(len(vals)-1):
    for j in range(i+1,len(vals)):
        if vals[i]>vals[j]:
            vals[i],vals[j]=vals[j],vals[i]

out=[0]
if len(vals) > K:
    def accum(acc,x): acc[0]+=x; return acc
    reduce(accum, vals[:len(vals)-K], out)
print(out[0])