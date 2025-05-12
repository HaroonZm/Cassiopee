S = input()

check = 0
count = 0
for i in range(len(S)):
    if check == int(S[i]):
        count += 1
    check = 1-check

check = 1
count2 = 0
for i in range(len(S)):
    if check == int(S[i]):
        count2 += 1
    check = 1-check

print(len(S) - max(count, count2))