ch = input()
i = 0
while i < len(ch):
    num = ord(ch[i])
    if num >= 68:
        num = num - 3
    else:
        num = num + 23
    ans = chr(num)
    print(ans, end='')
    i = i + 1
print()