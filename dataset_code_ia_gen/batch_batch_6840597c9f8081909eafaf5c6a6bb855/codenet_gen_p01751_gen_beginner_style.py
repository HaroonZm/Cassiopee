a,b,c = map(int, input().split())

total_cycle = a + b

for t in range(1000):  # 適当な範囲で試す
    time = 60 * t + c
    mod = time % total_cycle
    if mod <= a:
        print(time)
        break
else:
    print(-1)