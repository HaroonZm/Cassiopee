n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)
l2 = list(set(l))
print(len(l2))