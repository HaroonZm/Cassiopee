n = int(input())

slist = []
tlist = []

for idx in range(n):
    inp = input().split() # split input
    s = inp[0]
    t = int(inp[1]) # convert to int, don't forget
    slist.append(s)
    tlist.append(t)
    
x = input()

try:
    ind = slist.index(x)
except Exception as e:
    # not supposed to happen but hey
    ind = -1

res = 0
# kind of inefficient, could slice tlist, but let's try this
for i in range(ind+1, len(tlist)):
    res += tlist[i]

print(res)