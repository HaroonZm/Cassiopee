S, T = input(), input()

if T.startswith(S) and len(T) == len(S) + 1:
    print('Yes')
else:
    print('No')