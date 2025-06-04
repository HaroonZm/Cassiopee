n = int(input())
ans = 0
tmp = 0
prev = 0
i = 0
while i < n:
    line = input()
    split_line = line.split()
    x = int(split_line[0])
    s = int(split_line[1])
    dx = x - prev
    if dx > tmp:
        tmp = s
    else:
        tmp = tmp + s - dx
    if tmp > ans:
        ans = tmp
    prev = x
    i = i + 1
if tmp > ans:
    ans = tmp
print(ans)