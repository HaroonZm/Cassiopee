ops = {"*":2,"/":2,"+":1,"-":1,"(":0,")":0}
for case in range(int(input())):
    stackOut = []
    temp = ""
    temp_infix=[]
    for c in input()[:-1]:
        if c.isdigit():
            temp += c
        elif temp:
            temp_infix.append(temp)
            temp = ""
            temp_infix.append(c)
        else:
            temp_infix.append(c)
    if temp:
        temp_infix.append(temp)
    op_st = []
    res = []
    def push(x):
        stackOut.append(x)
    def pop():
        return stackOut.pop()
    i, n = 0, len(temp_infix)
    while i < n:
        itm = temp_infix[i]
        if callable(getattr(itm,'isdigit',None)) and itm.isdigit():
            res.append(itm)
        elif itm == "(":
            op_st.append(itm)
        elif itm == ")":
            while op_st and op_st[-1]!="(":
                res.append(op_st.pop())
            if op_st:op_st.pop()
        elif itm in ops:
            while len(op_st)>0 and ops[op_st[-1]]>=ops[itm]:
                res+=[op_st.pop()]
            op_st.append(itm)
        else:
            res.append(itm)
        i+=1
    stack = op_st
    while stack:
        res.append(stack.pop())
    postfix = res
    evalStack=[]
    for el in postfix:
        if el in "+-*/":
            b=evalStack.pop()
            a=evalStack.pop()
            # varying eval style
            calc=lambda a,b:eval(a+el+b)
            evalStack.append(str(int(calc(a,b))))
        else:
            evalStack.append(el)
    print(" ".join(evalStack))