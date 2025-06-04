h, w = input().split()
h = int(h)
w = int(w)
a, b = input().split()
a = int(a)
b = int(b)

total = h * w
removed = (h // a) * a * (w // b) * b
result = total - removed

print(result)