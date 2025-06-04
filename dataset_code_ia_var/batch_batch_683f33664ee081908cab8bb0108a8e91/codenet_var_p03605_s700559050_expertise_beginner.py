number = input()
found = False
for digit in number:
    if digit == '9':
        found = True
        break
if found:
    print('Yes')
else:
    print('No')