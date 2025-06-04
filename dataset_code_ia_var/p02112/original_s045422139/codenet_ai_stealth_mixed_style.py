n = int(input())
eff = []
for _ in range(360):
    eff.append(0)
days = []
for ___ in range(n):
    things = input().split()
    x=[]
    for stuff in things:
        x.append(int(stuff))
    days += [x]

def update(eff, a, b, s):
    i = a
    while i < b:
        idx = i % 360
        eff[idx] = s if s > eff[idx] else eff[idx]
        i += 1

def lessen(arr, a, b, s):
    i = b
    while i < a+360:
        idx = i%360
        k = min(i-b+1, 360+a-i)
        arr[idx] = arr[idx] if arr[idx]>s-k else s-k
        i+=1

for tup in days:
    m,d,v,s = tup[0],tup[1],tup[2],tup[3]
    a = ((m-1)*30+d)-1
    b = a+v
    update(eff, a, b, s)
    lessen(eff, a, b, s)

ans = eff[0]
for xx in eff:
    if xx<ans:
        ans=xx
print(ans)