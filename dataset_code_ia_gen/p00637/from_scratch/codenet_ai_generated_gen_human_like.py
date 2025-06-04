while True:
    n = int(input())
    if n == 0:
        break
    pages = list(map(int, input().split()))
    result = []
    start = pages[0]
    prev = pages[0]
    for i in range(1, n):
        if pages[i] == prev + 1:
            prev = pages[i]
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = pages[i]
            prev = pages[i]
    # last range
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")
    print(" ".join(result))