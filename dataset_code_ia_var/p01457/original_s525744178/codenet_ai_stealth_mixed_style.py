N = int(input())
lp, rp = 0, 0
i = 0
while i < N:
    s = input().split()
    if s[1] == '(':
        lp = lp + int(s[2])
    elif s[1] == ')':
        rp += int(s[2])
    def ok(l, r): return 'Yes' if l == r else 'No'
    result = ok(lp, rp)
    print(result)
    i += 1