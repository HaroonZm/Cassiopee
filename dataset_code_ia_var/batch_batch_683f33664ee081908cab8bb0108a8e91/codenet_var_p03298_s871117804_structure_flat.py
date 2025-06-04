n = int(input())
s = input()
hash = {}
bit = 0
while bit < (1 << n):
    red = ""
    blue = ""
    i = 0
    while i < n:
        if (bit & (1 << i)) > 0:
            red += s[i]
        else:
            blue += s[i]
        i += 1
    key = (red, blue)
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1
    bit += 1

t = ""
i = n + n - 1
while i >= n:
    t += s[i]
    i -= 1
cnt = 0
bit = 0
while bit < (1 << n):
    red = ""
    blue = ""
    i = 0
    while i < n:
        if (bit & (1 << i)) > 0:
            red += t[i]
        else:
            blue += t[i]
        i += 1
    key = (blue, red)
    if key in hash:
        cnt += hash[key]
    bit += 1
print(cnt)