while 1:
    s=input()
    if s=='.':
        break
    stk=[]
    try:
        for c in s:
            if c in '([':
                stk.append(c)
            elif c == ')' and stk[-1]=='(':
                del stk[-1]
            elif c == ']' and stk[-1]=='[':
                del stk[-1]
            elif c in '()[]':
                print('no')
                break
        else:
            if len(stk)==0:
                print('yes')
            else:
                print('no')
    except:
        print('no')