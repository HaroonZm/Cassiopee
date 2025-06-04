S = input()
from collections import Counter
c = Counter(S)
letters = sorted([ch*c[ch] for ch in c if ch.isalpha()])
digits = sorted([ch*c[ch] for ch in c if ch.isdigit()])
s = ''.join(letters)+''.join(digits)
res = 0
i = 0
n = len(s)
while i < n:
    start = s[i]
    j = i+1
    while j < n:
        if start.isalpha() and s[j].isalpha() and ord(s[j])==ord(s[j-1])+1:
            j += 1
        elif start.isdigit() and s[j].isdigit() and int(s[j])==int(s[j-1])+1:
            j += 1
        else:
            break
    length = j - i
    if length >= 3:
        res += 3
    else:
        res += length
    i = j
print(res)