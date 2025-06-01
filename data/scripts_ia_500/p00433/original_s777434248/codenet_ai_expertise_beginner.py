a = raw_input()
a = a.split()
a = [int(x) for x in a]

b = raw_input()
b = b.split()
b = [int(x) for x in b]

s = a[0] + a[1] + a[2] + a[3]
t = b[0] + b[1] + b[2] + b[3]

if s >= t:
    print(s)
else:
    print(t)