A, B, C, D = map(int, input())

r = A + B + C + D
if r == 7:
    print('{}+{}+{}+{}=7'.format(A, B, C, D))
    exit()
while True:
    if A + B + C - D == 7:
        print('{}+{}+{}-{}=7'.format(A, B, C, D))
        exit()
    elif A + B - C - D == 7:
        print('{}+{}-{}-{}=7'.format(A, B, C, D))
        exit()
    elif A - B - C - D == 7:
        print('{}-{}-{}-{}=7'.format(A, B, C, D))
        exit()
    elif A - B + C - D == 7:
        print('{}-{}+{}-{}=7'.format(A, B, C, D))
        exit()
    elif A - B - C + D == 7:
        print('{}-{}-{}+{}=7'.format(A, B, C, D))
        exit()
    elif A + B - C + D == 7:
        print('{}+{}-{}+{}=7'.format(A, B, C, D))
        exit()
    elif A - B + C + D == 7:
        print('{}-{}+{}+{}=7'.format(A, B, C, D))
        exit()
    exit()