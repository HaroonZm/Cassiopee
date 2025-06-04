h, w = input().split()
h = int(h)
w = int(w)

a, b = input().split()
a = int(a)
b = int(b)

rh = h % a
rw = w % b

result = rh * w + rw * h - rh * rw
print(result)