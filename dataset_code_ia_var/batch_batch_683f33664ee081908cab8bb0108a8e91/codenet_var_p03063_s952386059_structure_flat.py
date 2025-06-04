N = int(input())
S = input()
allblack = 0
i = 0
while i < N:
    if S[i] != '#':
        allblack += 1
    i += 1
answer = allblack
whitecount = allblack
blackcount = 0
i = 0
while i < N:
    if S[i] == '.':
        whitecount -= 1
    else:
        blackcount += 1
    tmp = blackcount + whitecount
    if tmp < answer:
        answer = tmp
    i += 1
print(answer)