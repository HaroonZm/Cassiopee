s = list(input())
t = list(input())

kotae = True

for i in range(len(s)):
    if s[i] != t[i]:
        kotae = False
        break

if kotae:
    print("Yes")
else:
    print("No")