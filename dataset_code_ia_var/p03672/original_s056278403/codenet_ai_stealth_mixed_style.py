s = input()

check = lambda m: all([s[i]==s[m+i] for i in range(m)]) if m else True

i = len(s) - 1
while i > 1:
    if not (i % 2):
        m = i // 2
        res = check(m)
        if res is True:
            print(i)
            break
    i -= 1