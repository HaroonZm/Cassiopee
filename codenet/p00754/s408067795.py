while True:
    s = input()
    if s == '.':
        break

    ans = True
    stack = []
    for i in s:
        if i == '[' or i == '(':
            tmp = 1
            if i == '[':
                tmp = -1
            if not len(stack) or stack[-1] * tmp < 0:
                stack.append(tmp)
            else:
                stack[-1] += tmp

        if i == ']' or i == ')':
            tmp = 1
            if i == ']':
                tmp = -1
            if not len(stack) or stack[-1] * tmp < 0:
                ans = False
                break
            else:
                stack[-1] -= tmp
                if not stack[-1]:
                    stack = stack[0:-1]

    if len(stack):
        ans = False

    print('yes' if ans else 'no')