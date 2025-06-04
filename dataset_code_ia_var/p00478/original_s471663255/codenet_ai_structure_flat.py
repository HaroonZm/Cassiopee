s = raw_input()
n = input()
ans = 0
i = 0
while i < n:
    r = raw_input()
    j = 0
    found = False
    while j < len(r):
        flag = True
        k = 0
        while k < len(s):
            ri = (j + k) % len(r)
            if r[ri] != s[k]:
                flag = False
            k += 1
        if flag:
            ans += 1
            found = True
            break
        j += 1
    i += 1
print ans