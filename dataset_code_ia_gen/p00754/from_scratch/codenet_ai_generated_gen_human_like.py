def is_balanced(line):
    stack = []
    pairs = {')': '(', ']': '['}
    for char in line:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

while True:
    line = input()
    if line == '.':
        break
    print("yes" if is_balanced(line[:-1]) else "no")