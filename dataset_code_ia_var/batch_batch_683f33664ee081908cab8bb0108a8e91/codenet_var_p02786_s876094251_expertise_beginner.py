H = int(input())
cnt = 0
total = 1
while H > 1:
    H = H // 2
    cnt = cnt + total
    total = total * 2
print(cnt + total)