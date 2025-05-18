t = 0
for x in map(int, list(input())):
    t += x

if (t % 9) == 0:
    print('Yes')
else:
    print('No')