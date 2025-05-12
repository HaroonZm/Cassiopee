n = input()
l = sorted(map(int, input().split()))
l_len = len(l)

a = 0
for i in range(0,l_len,2):
    a = a + l[i]

print(a)