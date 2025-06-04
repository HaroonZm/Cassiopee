l = list(map(int, input().split()))
a = l[0]
b = l[1]
x = l[2]
if a <= x and x <= b:
    print('Yes')
else:
    if b <= x and x <= a:
        print('Yes')
    else:
        print('No')