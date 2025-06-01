while True:
    n = int(input())
    if n == 0:
        break
    stars = list(map(int, input().split()))
    count = {}
    for color in stars:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    half = n / 2
    found = False
    for color in count:
        if count[color] > half:
            print(color)
            found = True
            break
    if not found:
        print("NO COLOR")