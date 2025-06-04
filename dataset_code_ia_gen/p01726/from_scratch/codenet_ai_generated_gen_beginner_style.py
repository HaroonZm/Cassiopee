S = input()
T = input()

count = 0
len_s = len(S)
len_t = len(T)

for i in range(len_s - len_t + 1):
    diff = 0
    for j in range(len_t):
        if S[i+j] != T[j]:
            diff += 1
            if diff > 1:
                break
    if diff == 1:
        count += 1

print(count)