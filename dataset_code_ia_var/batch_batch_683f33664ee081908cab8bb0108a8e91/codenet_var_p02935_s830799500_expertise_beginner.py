n = int(input())
liste = input().split()
v = []
for x in liste:
    v.append(int(x))
v.sort()
for i in range(n-1):
    v[i+1] = (v[i] + v[i+1]) / 2
print(v[n-1])