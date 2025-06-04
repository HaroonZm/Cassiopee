from itertools import takewhile

s = input()
n = len(s)
cnt = n // 2
if n % 2:
    c = s[cnt]
    match = lambda i: cnt + i < n and cnt - i >= 0 and s[cnt + i] == s[cnt - i] == c
    i = sum(1 for _ in takewhile(match, range(n)))
else:
    c = s[cnt]
    match = lambda i: cnt + i < n and cnt - i - 1 >= 0 and s[cnt + i] == s[cnt - 1 - i] == c
    i = sum(1 for _ in takewhile(match, range(n)))
print(cnt + i)