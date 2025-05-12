H = int(input())
cnt = 0
total = 1
while 1 < H:
    H = H // 2
    cnt += total
    total *= 2
print(cnt + total)