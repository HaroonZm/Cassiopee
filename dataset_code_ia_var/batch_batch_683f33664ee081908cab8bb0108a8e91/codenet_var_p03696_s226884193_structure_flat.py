n = int(input())
s = input()
l_num = 0
r_num = 0
i = 0
while i < len(s):
    if s[i] == '(':
        l_num += 1
    elif l_num <= 0:
        r_num += 1
    else:
        l_num -= 1
    i += 1
print('(' * r_num + s + ')' * l_num)