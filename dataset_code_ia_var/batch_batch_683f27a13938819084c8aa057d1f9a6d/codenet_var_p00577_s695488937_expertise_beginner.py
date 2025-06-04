n = int(input())
s = input()
i = 0
count = 0
while i < n - 1:
    if (s[i] == 'O' and s[i+1] == 'X') or (s[i] == 'X' and s[i+1] == 'O'):
        count = count + 1
        i = i + 2
    else:
        i = i + 1
print(count)