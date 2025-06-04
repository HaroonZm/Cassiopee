line = input()
lebel = 0
for i in range(len(line)):
    if line[i] == '*':
        print(lebel)
        break
    if line[i] == '(':
        lebel += 1
    elif line[i] == ')':
        lebel -= 1