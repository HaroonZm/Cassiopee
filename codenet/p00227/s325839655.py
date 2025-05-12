while True:
    try:
        num, size = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort(reverse = True)
        for i in range(size-1, num, size):
            arr[i] = 0
        print(sum(arr))
    except:
        break