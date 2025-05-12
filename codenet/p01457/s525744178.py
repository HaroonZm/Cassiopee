N = int(input())
lp = rp = 0
for i in range(N):
    p,c,n = input().split()
    if c == '(':
        lp += int(n)
    else:
        rp += int(n)
    print('Yes' if lp == rp else 'No')