S = input()
if S[0] == S[1] == S[2]:
    print(S)
else:
    if int(S) > int(S[0] * 3):
        print(int(S[0] * 3) + 111)
    else:
        print(int(S[0] * 3))