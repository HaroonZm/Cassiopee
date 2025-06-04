a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
ans = ""

i = 0
while i < c - a:
    ans = ans + "R"
    i = i + 1

j = 0
while j < d - b:
    ans = ans + "U"
    j = j + 1

i = 0
while i < c - a:
    ans = ans + "L"
    i = i + 1

j = 0
while j < d - b:
    ans = ans + "D"
    j = j + 1

ans = ans + "D"

i = 0
while i < (c - a + 1):
    ans = ans + "R"
    i = i + 1

j = 0
while j < (d - b + 1):
    ans = ans + "U"
    j = j + 1

ans = ans + "LU"

i = 0
while i < (c - a + 1):
    ans = ans + "L"
    i = i + 1

j = 0
while j < (d - b + 1):
    ans = ans + "D"
    j = j + 1

ans = ans + "R"

print(ans)