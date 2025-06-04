while True:
    try:
        num = int(input())
    except:
        break
    i = 0
    while i < num:
        s = input()
        print(s.replace('Hoshino', 'Hoshina'))
        i += 1