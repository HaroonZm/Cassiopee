n = input()
a = []
b = []
c = 0
for i in range(len(n)):
    if n[i] == "," or n[i] == "." or n[i] == " ":
        if c >= 3 and c <= 6:
            b = b + a + [" "]
        a = []
        c = 0
    else:
        a.append(n[i])
        c += 1
if len(b) > 0:
    b.pop()
for i in range(len(b)):
    print(b[i], end="")
print()