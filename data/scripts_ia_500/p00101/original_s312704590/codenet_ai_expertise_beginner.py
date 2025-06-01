while True:
    try:
        num = int(input())
    except:
        break
    for i in range(num):
        line = input()
        new_line = line.replace('Hoshino', 'Hoshina')
        print(new_line)