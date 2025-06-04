a = [0, 0, 0, 0]
aa = ["A", "B", "AB", "O"]
while True:
    try:
        s = input()
    except:
        break
    parts = s.split(",")
    b = parts[0]
    c = parts[1]
    for i in range(len(aa)):
        if c == aa[i]:
            a[i] = a[i] + 1
for i in range(4):
    print(a[i])