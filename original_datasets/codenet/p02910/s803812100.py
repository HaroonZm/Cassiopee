def Inn(s):
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] not in ['R', 'U', 'D']:
                return "No"
        else:
            if s[i] not in ['L', 'U', 'D']:
                return "No"
    return "Yes"

s = input()
print(Inn(s))