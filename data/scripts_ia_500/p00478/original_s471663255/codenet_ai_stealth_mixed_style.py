s = raw_input()
n = int(input())
counter = 0
for i in range(n):
    r = raw_input()
    found = False
    j = 0
    while j < len(r) and not found:
        flag = True
        for k in xrange(len(s)):
            ri = (j + k) % len(r)
            if r[ri] != s[k]:
                flag = False
                break
        if flag:
            counter += 1
            found = True
        j += 1
print counter