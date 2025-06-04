n = int(input())
for i in range(1<<n):
    ans = []
    tmp = i
    cnt = 0
    j = i
    while j:
        if j & 1:
            ans.append(cnt)
        cnt += 1
        j = j >> 1
    print(f"{tmp}:", end = '')
    if tmp == 0:
        print()
    else:
        print("", *ans)