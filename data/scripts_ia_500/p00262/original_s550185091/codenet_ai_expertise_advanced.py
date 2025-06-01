tri_num = {i*(i+1)//2 for i in range(1, 100000)}
l = list(range(1, 100000))

while (N := int(input())) != 0:
    b = list(map(int, input().split()))
    if sum(b) not in tri_num:
        print(-1)
        continue

    ans = 0
    length = len(b)
    target = l[:length]

    while ans <= 10000:
        if b == target:
            print(ans)
            break
        b = [x - 1 for x in b if x > 1] + [length]
        length = len(b)
        target = l[:length]
        ans += 1
    else:
        print(-1)