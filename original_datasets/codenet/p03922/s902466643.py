from collections import Counter
n, m = map(int,input().split())
x = list(map(int,input().split()))
data = [[] for i in range(m)]

def mod(x):
    return x%m - 1
def insert(x):
    y = mod(x)
    data[y].append(x)
for i in x:
    insert(i)

ans = len(data[m-1])//2

#print(data)

for i in range(m//2):
    p = len(data[i])
    q = len(data[m-i-2])
    if  p == q:
        if i != m-i-2:
            ans += p
        else:
            ans += p//2
    elif p > q:
        ans += q
        r = (p-q)//2
        same = 0
        set_i = Counter(data[i])
        for keys in set_i:
            same +=set_i[keys]//2
        #print(set_i)
        ans += min(r,same)
    else:
        ans += p
        r = (q-p)//2
        set_j = Counter(data[m-i-2])
        same = 0
        for keys in set_j:
            same += set_j[keys] // 2
        #print(set_j)
        ans += min(r,same)

print(ans)