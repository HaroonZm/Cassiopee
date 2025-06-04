c = "w kstnhmyr"
v = "aiueo"
d = ["T", "L", "U", "R", "D"]
f = []
a = input()
i = 0
while i < len(a):
    b = int(a[i])
    e = d.index(a[i+1])
    if b == 0 and e == 2:
        f.append("nn")
    elif b == 1:
        f.append(v[e])
    else:
        f.append(c[b] + v[e])
    i = i + 2
print("".join(f))