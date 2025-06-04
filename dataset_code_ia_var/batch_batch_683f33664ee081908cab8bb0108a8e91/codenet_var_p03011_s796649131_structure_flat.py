inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a + b)