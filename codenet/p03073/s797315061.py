s = input()
count = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        if s[i - 1] == '0':
            s = s[:i] + '1' + s[i + 1:]
        else:
            s = s[:i] + '0' + s[i + 1:]
print(count)