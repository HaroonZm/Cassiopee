li = ['KIHBR', 'KIHBRA', 'KIHBAR', 'KIHBARA', 'KIHABR', 'KIHABRA', 'KIHABAR', 'KIHABARA']
S = input()

if S in li:
    print('YES')
else:
    if len(S) > 1:
        if S[0] == 'A' and S[1:] in li:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')