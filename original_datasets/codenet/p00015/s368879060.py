n = input()
for k in range(n):
    a = input()
    b = input()
    c = int(a) + int(b)
    if len(str(c)) > 80:
        c = "overflow"
    print c