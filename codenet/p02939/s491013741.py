from collections import defaultdict
s = input()

head = 0
tail = 1
ans = 0
before = ""
while True:
    ss = s[head:tail]
    if ss != before:
        before = ss
        head = tail
        tail = head + 1
        ans += 1
    else:
        tail += 1
    if tail == len(s)+1:
        print(ans)
        exit()