n = int(raw_input())
k = 0
while k < n:
    a = raw_input()
    b = raw_input()
    c = int(a) + int(b)
    c_str = str(c)
    if len(c_str) > 80:
        c = "overflow"
    print c
    k += 1