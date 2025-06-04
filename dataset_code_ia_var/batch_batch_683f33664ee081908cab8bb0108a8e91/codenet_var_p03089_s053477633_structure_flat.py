N = int(input())
b = list(map(int, input().split(' ')))
buf = []
for _ in range(N):
    is_end = True
    for i in range(len(b)-1, -1, -1):
        if i+1 == b[i]:
            buf.append(b[i])
            b.pop(i)
            is_end = False
            break
    if is_end:
        print(-1)
        exit()
i = len(buf) - 1
while i >= 0:
    print(buf[i])
    i -= 1