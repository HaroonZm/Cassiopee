S = input()
star_pos = S.index('*')
count = 0
for i in range(star_pos - 1, -1, -1):
    if S[i] == '(':
        j = star_pos + 1
        level = 1
        valid = True
        while j < len(S) and level > 0:
            if S[j] == '(':
                level += 1
            elif S[j] == ')':
                level -= 1
            j += 1
        if level == 0 and S[j - 1] == ')':
            count += 1
print(count)