n = int(input())
a = []
for z in input().split(): a.append(int(z))
result = ""
stack = []
cnt = 0

def add_left_parens(target):
    nonlocal cnt, result, stack
    while cnt < target:
        result += '('
        cnt += 1
        stack.extend([cnt])

for idx in range(len(a)):
    add_left_parens(a[idx])
    try:
        if stack and stack[-1] == a[idx]:
            stack.pop()
            result = result + ")"
        else:
            result = ":("
            break
    except Exception:
        result = ":("
        break
print(result)