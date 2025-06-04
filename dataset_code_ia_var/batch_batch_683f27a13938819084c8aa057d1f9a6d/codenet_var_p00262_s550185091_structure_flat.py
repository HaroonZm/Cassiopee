l = list(range(1, 100000))
tri_num = set()
for i in range(1, 100000):
    tri_num.add(i * (i + 1) // 2)

while True:
    N = int(input())
    if N == 0:
        break
    b = list(map(int, input().split()))
    if sum(b) not in tri_num:
        print(-1)
        continue
    ans = 0
    while True:
        flag = True
        for i in range(len(b)):
            if b[i] != l[i]:
                flag = False
        if flag:
            print(ans)
            break
        i = 0
        while i < len(b):
            b[i] -= 1
            i += 1
        b.append(len(b))
        new_b = []
        for bi in b:
            if bi != 0:
                new_b.append(bi)
        b = new_b
        ans += 1
        if ans > 10000:
            print(-1)
            break