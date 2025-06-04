c = "w kstnhmyr"
v = "aiueo"
d = ["T", "L", "U", "R", "D"]
f = ""
a = input()
i = 0
while i < len(a):
    b = int(a[i])
    e = d.index(a[i+1])
    if b == 0 and e == 2:
        f = f + "nn"
    elif b == 1:
        f = f + v[e]
    else:
        f = f + c[b] + v[e]
    i = i + 2
print(f)