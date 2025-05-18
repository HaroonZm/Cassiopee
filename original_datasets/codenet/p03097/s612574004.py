def split(n, a, b, remain, ai, ans, width, l=None):
    # print(n, a, b, remain, ai, ans, width)
    # print(*(f'{c:5d}' for c in ans))
    # print(*(f'{c:05b}' for c in ans))
    if width == 2:
        ans[ai] = a
        ans[ai + 1] = b
        return
    if l is None:
        x = a ^ b
        y = x & -x  # Rightmost Bit at which is different for a and b
        l = y.bit_length() - 1
    else:
        y = 1 << l
    remain.remove(l)
    i = next(iter(remain))
    lb = a ^ (1 << i)
    ra = lb ^ y
    width >>= 1
    split(n, a, a ^ (1 << i), remain, ai, ans, width, i)
    split(n, ra, b, remain, ai + width, ans, width)
    remain.add(l)

def solve(n, a, b):
    if bin(a).count('1') % 2 == bin(b).count('1') % 2:
        print('NO')
        return
    remain = set(range(n))
    ans = [0] * (1 << n)
    split(n, a, b, remain, 0, ans, 1 << n)
    print('YES')
    print(*ans)

n, a, b = list(map(int, input().split()))
solve(n, a, b)