N = input()
S = input()

min_num = 300000

for i in range(len(S)):
    left = 0
    right = 0

    for j in range(i):
        if S[j] == 'W':
            left += 1

    for j in range(i + 1, len(S)):
        if S[j] == 'E':
            right += 1

    if left + right < min_num:
        min_num = left + right

print(min_num)