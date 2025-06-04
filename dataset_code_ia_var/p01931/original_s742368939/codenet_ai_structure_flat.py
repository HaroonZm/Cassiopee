n = int(input())
s = input()
i = 0
while i < n - 1:
    if s[i] == 'x' and s[i+1] == 'x':
        n = i + 1
        i = n  # force exit
    else:
        i += 1
print(n)