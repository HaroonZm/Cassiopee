while True:
    string = input()
    if string == 'END OF INPUT':
        break
    ans = []
    temp = 0
    space = 0
    for i in range(len(string)):
        if string[i] == ' ' and space == 0:
            ans.append(temp)
            temp = 0
            space = 1
            continue
        elif space > 0 and string[i] == ' ':
            ans.append(0)
            continue
        space = 0
        temp += 1
    ans.append(temp)
    print(''.join(str(x) for x in ans))