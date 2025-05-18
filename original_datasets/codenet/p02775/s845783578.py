s = input()[::-1]
size = len(s)
s += "4"

a, b = 0, 0

for i in range(size):
    v1, v2 = int(s[i]), int(s[i+1])
    if v1+b>=6 or (v1+b>=5 and v2>=5):
        a += 10-v1-b
        b = 1
    else:
        a += v1+b
        b = 0

print(a+b)