while True:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0:
        break
    a_str = input().split()
    a = []
    for i in range(len(a_str)):
        a.append(int(a_str[i]))
    c = 0
    for i in range(n):
        part = m // n
        if a[i] < part:
            c = c + a[i]
        else:
            c = c + part
    print(c)