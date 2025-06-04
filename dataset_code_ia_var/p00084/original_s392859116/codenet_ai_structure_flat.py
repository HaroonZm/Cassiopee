n = list(input())
a = []
b = []
c = 0
i = 0
while i < len(n):
    if n[i] == "," or n[i] == "." or n[i] == " ":
        if c >= 3 and c <= 6:
            b = b + a + [" "]
        a = []
        c = 0
    else:
        a.append(n[i])
        c = c + 1
    i = i + 1
if len(b) > 0:
    del b[-1]
j = 0
while j < len(b):
    print(b[j], end="")
    j = j + 1
print()