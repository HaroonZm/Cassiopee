ch = input()
for i in range(len(ch)):
    num = ord(ch[i])
    if num>=68:
        num -= 3
    else:
        num += 23
    ans = chr(num)
    print(ans, end='')
print()