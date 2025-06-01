while True:
    n = input()
    if n == '0':
        break
    s = []
    for i in range(int(n)):
        line = input()
        parts = line.split()
        parts = [int(x) for x in parts]
        s.append(parts)
    r_line = input()
    r = r_line.split()
    r = [int(x) for x in r]
    flag = 0
    for i in s:
        if i[1] <= r[0] and i[2] <= r[1] and i[3] <= r[2] and 4*(i[1] + i[3]) + 9*i[2] <= r[3]:
            print(i[0])
            flag = 1
    if flag == 0:
        print("NA")