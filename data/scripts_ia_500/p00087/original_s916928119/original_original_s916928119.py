while True :
    try :
        lst = list(input().split())
    except EOFError :
        break
    
    stack = []
    for i in lst :
        if i == '+' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            stack.append(a+b)
        elif i == '-' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            stack.append(a-b)
        elif i == '*' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            stack.append(a*b)
        elif i == '/' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            stack.append(a/b)
        else :
            stack.append(int(i))
    print('{:.8f}'.format(stack[0]))