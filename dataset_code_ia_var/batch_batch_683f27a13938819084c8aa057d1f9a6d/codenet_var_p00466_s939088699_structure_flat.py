while True:
    s = input()
    if not s:
        break
    i = 0
    while i < 9:
        s = s - input()
        i = i + 1
    print(s)