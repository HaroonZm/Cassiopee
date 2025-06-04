N = int(input())
S = input()

count = 0
consecutive_wrong = 0

for c in S:
    if consecutive_wrong == 2:
        break
    if c == 'x':
        consecutive_wrong += 1
    else:
        consecutive_wrong = 0
    count += 1

print(count)