# B
# 2020/3/9  17:57-
n = int(input())
l = []
for i in range(n):
    ss, pp = map(str, input().split())
    l.append([ss, int(pp), i])
    
l.sort(key=lambda x: x[1], reverse=True)
l.sort(key=lambda x: x[0])

for v in l:
    print(v[2]+1)