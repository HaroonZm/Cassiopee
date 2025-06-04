s = list(input())
t = list(input())
if s[0] == t[2]:
    if s[2] == t[0]:
        if s[1] == t[1]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')