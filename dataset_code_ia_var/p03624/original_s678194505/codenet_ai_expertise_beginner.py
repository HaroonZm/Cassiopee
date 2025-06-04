S = input()
alphabet = []
for i in range(26):
    alphabet.append(chr(97 + i))
ans = []
for a in alphabet:
    if a not in S:
        ans.append(a)
if len(ans) == 0:
    print('None')
else:
    print(ans[0])