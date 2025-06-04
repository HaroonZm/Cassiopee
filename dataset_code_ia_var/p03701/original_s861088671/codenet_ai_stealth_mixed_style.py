a = []
for i in range(int(raw_input())):
    a.append(int(raw_input()))
a.append(0)
s = 0
for x in a:
    s += x
z = 0
i = 0
while i < len(a):
    candidate = s - a[i]
    if candidate % 10 > 0:
        if candidate > z:
            z = candidate
    i += 1
print(z)