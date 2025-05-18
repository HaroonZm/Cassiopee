s = list(input())

base = ['A', 'T', 'C', 'G']

a = -1
b = -1

L = 0
R = -1
mode = 1
for i in range(len(s)):
    if mode == 0:
        if s[i] in base:
            b += 1
        else:
            mode = 1
            if b - a > R - L:
                L = a
                R = b
    elif mode == 1:
        if s[i] in base:
            a = i
            b = i
            mode = 0

if mode == 0 and b - a > R - L:
    L = a
    R = b

print(R - L + 1)