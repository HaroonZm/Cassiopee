def main():
    S = input()
    if len(S) == 1:
        return 1
    dp_1 = [0] * len(S)
    dp_2 = [0] * len(S)
    if S[0] != S[1]:
        dp_1[1] = 2
    dp_1[0] = 1
    dp_2[1] = 1
    for i in range(len(S)):
        if i < 2:
            continue
        if S[i] == S[i-1]:
            dp_1[i] = dp_2[i-1] + 1
        else:
            if dp_1[i-1] > dp_2[i-1]:
                dp_1[i] = dp_1[i-1] + 1
            else:
                dp_1[i] = dp_2[i-1] + 1
        if i < 4 or S[i-1:i+1] == S[i-3:i-1]:
            dp_2[i] = dp_1[i-2] + 1
        else:
            if dp_1[i-2] > dp_2[i-2]:
                dp_2[i] = dp_1[i-2] + 1
            else:
                dp_2[i] = dp_2[i-2] + 1
    if dp_1[-1] > dp_2[-1]:
        return dp_1[-1]
    else:
        return dp_2[-1]

print(main())