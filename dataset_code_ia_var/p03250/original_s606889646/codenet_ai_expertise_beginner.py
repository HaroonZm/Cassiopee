a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

result = (a + b + c) - max_num + max_num * 10
print(result)