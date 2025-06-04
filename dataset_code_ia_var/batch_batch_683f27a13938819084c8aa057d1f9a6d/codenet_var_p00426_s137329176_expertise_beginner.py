ans = []
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    a = 0
    b = 0
    c = 0
    for i in range(3):
        A = list(map(int, input().split()))
        if A[0] != 0:
            for j in range(1, A[0]+1):
                if i == 0:
                    a += 2**(A[j]-1)
                elif i == 1:
                    b += 2**(A[j]-1)
                else:
                    c += 2**(A[j]-1)
    queue = []
    queue.append((0, a, b, c, ""))
    found = False
    while len(queue) > 0:
        cnt, a, b, c, prev = queue.pop(0)
        if cnt > M:
            ans.append(-1)
            found = True
            break
        if a+b == 0 or b+c == 0:
            ans.append(cnt)
            found = True
            break
        if a == 0:
            amax = -1
        else:
            num = a
            amax = 0
            while num > 1:
                num = num // 2
                amax += 1
        if b == 0:
            bmax = -1
        else:
            num = b
            bmax = 0
            while num > 1:
                num = num // 2
                bmax += 1
        if c == 0:
            cmax = -1
        else:
            num = c
            cmax = 0
            while num > 1:
                num = num // 2
                cmax += 1
        # ab or ba
        if amax > bmax and prev != 'ba':
            queue.append((cnt+1, a - 2**amax, b + 2**amax, c, 'ab'))
        elif amax < bmax and prev != 'ab':
            queue.append((cnt+1, a + 2**bmax, b - 2**bmax, c, 'ba'))
        # cb or bc
        if cmax > bmax and prev != 'bc':
            queue.append((cnt+1, a, b + 2**cmax, c - 2**cmax, 'cb'))
        elif cmax < bmax and prev != 'cb':
            queue.append((cnt+1, a, b - 2**bmax, c + 2**bmax, 'bc'))
print('\n'.join(map(str, ans)))