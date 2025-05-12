N = int(input())
V = [int(i) for i in input().split(" ")]
V.sort()
m = V[0]
for i in range(1,len(V)):
    m = (m + V[i])/2
print(m)