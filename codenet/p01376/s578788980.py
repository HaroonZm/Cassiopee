m,n=map(int, input().split())
s = []
for i in range(m):
    s.append(sum(list(map(int,input().split()))))
print(max(s))