bw = input()
cnt = 0
t = bw[0]
for i in range(1, len(bw)):
    if bw[i] != t:
        cnt = cnt + 1
        t = bw[i]
print(cnt)