while True:
    try:
        num = int(input())
    except:
        break
    times = list(map(int, input().split()))
    times.sort()
    ans = sum([(num-index) * time for index, time in enumerate(times)])
    print(ans)