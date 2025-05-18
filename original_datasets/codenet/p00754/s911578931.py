while True :
    s = input()
    tmp = []
    if s == '.' :
        break
    ans = True
    for i in range(len(s)) :
        if s[i] == '(' :
            tmp.append(s[i])
        elif s[i] == '[' :
            tmp.append(s[i])
        elif s[i] == ')' :
            if '(' not in tmp :
                ans = False
                break
            elif tmp[-1] == '(' :
                tmp.pop(-1)
            else :
                ans = False
                break
        elif s[i] == ']' :
            if '[' not in tmp :
                ans = False
                break
            elif tmp[-1] == '[' :
                tmp.pop(-1)
            else :
                ans = False
                break
    if len(tmp) != 0 or ans == False :
        print('no')
    else :
        print('yes')