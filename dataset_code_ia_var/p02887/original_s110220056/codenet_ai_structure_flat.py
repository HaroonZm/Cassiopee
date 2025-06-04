n = int(input())
s = input()
li = []
answer = 0
temp = ''
i = 0
while i < len(s):
    if temp == s[i]:
        i += 1
        continue
    else:
        temp = s[i]
        answer += 1
        i += 1
print(answer)