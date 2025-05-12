n = int(input())
# a = list(map(int, input()split()))
for i in range(1<<n):
    ans = []
    _i = i
    cnt = 0
    while i:
        if i&1:
            ans.append(cnt)
        cnt += 1
        i=i>>1
    print(f'{_i}:',end = '')
    if _i == 0:
        print()
    else:print("",*ans)