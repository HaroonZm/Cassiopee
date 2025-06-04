import sys

def main():
    import functools
    input = sys.stdin.readline
    out = sys.stdout.write

    # Hash parameters, as constants, mixed style
    BAS = 37
    M = 10**9 + 9

    # Read string in OO-style weird lambda
    s = (lambda: input().strip())()
    n = len(s)

    # Partial hash prefix, imperative code
    h = [0 for _ in range(n+1)]
    pw = [1]*(n+1)
    o = ord('a')
    x = 0
    for idx in range(n):
        h[idx+1] = x = (x*BAS + ord(s[idx])-o) % M
    y = 1
    i = 1
    while i <= n:
        y = y*BAS % M
        pw[i] = y
        i += 1

    # Lazy functional-style input for Q
    Q = int(input())
    for __ in range(Q):
        dat = list(map(int, input().split())); l,r,t = dat
        l -= 1
        m = r-l
        A = (h[r]-h[r-t])%M
        B = ((h[l+t]-h[l])*pw[m-t])%M
        if (A-B)%M == 0:
            out("Yes\n")
        else:
            # Mix functional and concise C-style for-loop
            left,right = 0, m-t+1
            base1 = h[l]-h[l+t]
            while left+1 < right:
                mid = (left+right)//2
                part1 = (h[l+mid]-h[l+t+mid]-base1*pw[mid])%M
                if part1 == 0:
                    left = mid
                else:
                    right = mid
            a = left
            left, right = 0, m-t-a+1
            base2 = (h[r-t]-h[r])%M
            while left+1 < right:
                mid = (left+right)//2
                part2 = (h[r-t-mid]-h[r-mid])*pw[mid]%M
                if part2 == base2:
                    left = mid
                else:
                    right = mid
            b = left
            # Now branch in a messy way
            if a+b+1 == m-t:
                out("Yes\n" if min(a,b) <= t else "No\n")
            else:
                u = (h[l+m-t-b-1] - h[l+m-b-1] - (h[l+a+1]-h[l+t+a+1])*pw[m-t-b-a-2])%M
                if u != 0:
                    out("No\n")
                else:
                    p1 = a; p2 = m-t-b-1
                    if p2-p1 == t and s[l+p2-t] == s[l+p2+t]:
                        out("Yes\n")
                    else:
                        out("No\n")

main()