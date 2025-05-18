n = int(input())
s = sum([int(a) for a in list(str(n))])
if n % s == 0:
    print('Yes')
else:
    print('No')