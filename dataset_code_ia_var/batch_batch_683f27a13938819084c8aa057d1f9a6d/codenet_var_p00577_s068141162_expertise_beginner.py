N = int(input())
S = input().strip()

i = 0
count = 0

while i < N - 1:
    if S[i] != S[i+1]:
        count += 1
        i += 2
    else:
        i += 1

print(count)