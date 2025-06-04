while True:
    try:
        num = int(input())
    except:
        break
    times = input().split()
    for i in range(len(times)):
        times[i] = int(times[i])
    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            if times[j] < times[i]:
                temp = times[i]
                times[i] = times[j]
                times[j] = temp
    ans = 0
    for index in range(len(times)):
        ans += (num - index) * times[index]
    print(ans)