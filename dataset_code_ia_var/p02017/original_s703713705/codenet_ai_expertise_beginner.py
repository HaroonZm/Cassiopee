h, w, x, y = input().split()
h = int(h)
w = int(w)
x = int(x)
y = int(y)

if (h * w) % 2 == 1 and (x + y) % 2 == 1:
    print('No')
else:
    print('Yes')