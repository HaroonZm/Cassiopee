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

    # 終了条件
    if is_end:
        print(-1)
        exit()

for n in reversed(buf):
    print(n)