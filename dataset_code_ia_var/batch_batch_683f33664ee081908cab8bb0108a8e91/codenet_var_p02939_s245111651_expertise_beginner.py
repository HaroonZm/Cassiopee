s = input()
count = 1
i = 1
while i < len(s):
    if s[i] != s[i-1]:
        count = count + 1
        i = i + 1
    elif i < len(s) - 1 and s[i] == s[i-1]:
        count = count + 1
        i = i + 2
    else:
        break
print(count)