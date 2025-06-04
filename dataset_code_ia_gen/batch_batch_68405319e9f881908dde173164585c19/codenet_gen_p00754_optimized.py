while True:
    s = input()
    if s == '.':
        break
    stack = []
    balanced = True
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                balanced = False
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                balanced = False
                break
    if balanced and not stack:
        print("yes")
    else:
        print("no")