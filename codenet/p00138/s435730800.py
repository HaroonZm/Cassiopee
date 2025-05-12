data = []
tmp = []
ans = []

def pushAns(d):
    for j in range(2):
        ans.append((d[0][0],d[0][1]))
        d.pop(0)    

for i in range(24):
    a,b = (float(x) for x in input().split())
    tmp.append((a,b))
    if (i + 1) % 8 == 0:
        tmp.sort(key=lambda x:x[1])
        pushAns(tmp)
        data.extend(tmp)
        tmp.clear()
        
data.sort(key=lambda x:x[1])
pushAns(data)

for i in range(8):
    print(int(ans[i][0]),ans[i][1])