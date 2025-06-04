h, w, x, y = input().split()
h = int(h)
w = int(w)
x = int(x)
y = int(y)

result = (h * w) * (x + y)
if result % 2 == 1:
    print('No')
else:
    print('Yes')