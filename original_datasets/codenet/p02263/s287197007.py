cal = {
       "+": lambda a, b: b+a,
       "-": lambda a, b: b-a,
       "*": lambda a, b: b*a
       }

stack = []

for i in input().split():
    if i in cal:
        stack.append(cal[i](stack.pop(), stack.pop()))
    else:
        stack.append(int(i))

print(stack[-1])