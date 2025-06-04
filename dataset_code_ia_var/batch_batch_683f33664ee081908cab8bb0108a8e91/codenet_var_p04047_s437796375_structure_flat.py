n = input()
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
l_len = len(l)
a = 0
i = 0
while i < l_len:
    a = a + l[i]
    i = i + 2
print(a)