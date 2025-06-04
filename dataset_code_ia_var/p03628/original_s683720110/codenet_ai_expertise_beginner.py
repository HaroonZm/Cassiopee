import sys

n = int(sys.stdin.readline())
s = input()
t = input()

MOD = 10**9 + 7
v = 2
ans = 1
i = 0

while i < n:
    if s[i] == t[i]:
        # Vertical
        if v == 0:
            ans = ans * 2
        if v == 2:
            ans = ans * 3
        v = 0
        ans = ans % MOD
        i += 1
    else:
        # Horizontal
        if v == 0:
            ans = ans * 2
        if v == 1:
            ans = ans * 3
        if v == 2:
            ans = ans * 6
        v = 1
        ans = ans % MOD
        i += 2

print(ans % MOD)