S = input()
cnt, x = 0, 65
for c in S:
    cnt = cnt + (x >= ord(c))
    x = ord(c)
print(cnt)