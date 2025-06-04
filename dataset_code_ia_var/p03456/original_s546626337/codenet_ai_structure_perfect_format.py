a, b = map(int, input().split())
ab = str(a) + str(b)
flag = False

for i in range(1, 500):
    if i ** 2 == int(ab):
        flag = True

if flag:
    print('Yes')
else:
    print('No')