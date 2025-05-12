while True:
    try:
        num = int(input())
    except:
        break
    [print(input().replace('Hoshino', 'Hoshina')) for _ in range(num)]