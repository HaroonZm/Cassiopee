N = int(input())
number = list(map(int, input().split()))
a = number[-1]
del number[-1]

if number[0] == 0:
    N -= 1
    number.pop(0)

numbermap = []
for _ in range(N):
    row = []
    for __ in range(21):
        row.append(0)
    numbermap.append(row)

numbermap[0][0] = 1

i = 0
while i < N - 1:
    j = 0
    while j < 21:
        if j + number[i] <= 20:
            numbermap[i + 1][j + number[i]] = numbermap[i + 1][j + number[i]] + numbermap[i][j]
        if j - number[i] >= 0:
            numbermap[i + 1][j - number[i]] += numbermap[i][j]
        j += 1
    i += 1

print(numbermap[-1][a])