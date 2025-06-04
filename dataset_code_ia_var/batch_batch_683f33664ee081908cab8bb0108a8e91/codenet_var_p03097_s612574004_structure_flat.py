n, a, b = list(map(int, input().split()))
if bin(a).count('1') % 2 == bin(b).count('1') % 2:
    print('NO')
else:
    remain = set(range(n))
    ans = [0] * (1 << n)
    stack = []
    stack.append((n, a, b, remain.copy(), 0, ans, 1 << n, None))
    while stack:
        n1, a1, b1, remain1, ai1, ans1, width1, l1 = stack.pop()
        if width1 == 2:
            ans1[ai1] = a1
            ans1[ai1 + 1] = b1
            continue
        if l1 is None:
            x = a1 ^ b1
            y = x & -x
            l2 = y.bit_length() - 1
        else:
            y = 1 << l1
            l2 = l1
        remain1 = remain1.copy()
        remain1.remove(l2)
        i = next(iter(remain1))
        lb = a1 ^ (1 << i)
        ra = lb ^ y
        width2 = width1 >> 1
        # right
        stack.append((n1, ra, b1, remain1.copy(), ai1 + width2, ans1, width2, None))
        # left
        stack.append((n1, a1, a1 ^ (1 << i), remain1, ai1, ans1, width2, i))
    print('YES')
    print(*ans)