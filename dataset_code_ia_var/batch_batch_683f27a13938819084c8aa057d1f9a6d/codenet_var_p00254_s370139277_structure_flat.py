import copy

while True:
    n = list(input())
    if n == ["0", "0", "0", "0"]:
        break
    tmp = int(n[0]) * 1000 + int(n[1]) * 100 + int(n[2]) * 10 + int(n[3])
    if tmp % 1111 == 0:
        print("NA")
        continue
    cnt = 0
    while n != ["6", "1", "7", "4"]:
        for i in range(4):
            for j in range(i + 1, 4):
                if n[i] < n[j]:
                    n[i], n[j] = n[j], n[i]
        l = [x for x in n]
        for i in range(4):
            for j in range(i + 1, 4):
                if n[i] > n[j]:
                    n[i], n[j] = n[j], n[i]
        s = [x for x in n]
        l_int = int(l[0]) * 1000 + int(l[1]) * 100 + int(l[2]) * 10 + int(l[3])
        s_int = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])
        val = l_int - s_int
        n = list(str(val).zfill(4))
        cnt += 1
    print(cnt)