l = [0] * 100
l[0] = 2
l[1] = 1
for i in range(2, 90):
    l[i] = l[i-1] + l[i-2]

n = int(input())
print(l[n])