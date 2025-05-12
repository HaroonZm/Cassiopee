#B - Varied
S = list(input())

S_set = set(S)

if len(S) == len(S_set):
    print('yes')
else:
    print('no')