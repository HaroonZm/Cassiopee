x = input().split()
y = []
for i in x:
    y.append(int(i))
a = y[0]
b = y[1]
c = a - b
if c < 0:
    c = -c
print(c)