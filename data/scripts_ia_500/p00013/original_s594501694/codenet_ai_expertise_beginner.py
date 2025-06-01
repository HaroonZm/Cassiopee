train_list = []

while True:
    try:
        n = input()
        n = int(n)
    except EOFError:
        break
    if n == 0:
        if len(train_list) > 0:
            leaving = train_list.pop()
            print(leaving)
    else:
        train_list.append(n)