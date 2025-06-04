n = int(input())
s = input()
li = []
answer = 0
temp = ''
for i in s:
    if temp == i:
        continue
    else:
        temp = i
        answer += 1
print(answer)