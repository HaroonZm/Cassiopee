S = list(input())
check = 0

if 'E' in S :
    if 'W' in S:
        pass
    else:
        check = 1

if 'W' in S :
    if 'E' in S:
        pass
    else:
        check = 1

if 'N' in S :
    if 'S' in S:
        pass
    else:
        check = 1

if 'S' in S :
    if 'N' in S:
        pass
    else:
        check = 1

if check == 0:
    print('Yes')
else:
    print('No')