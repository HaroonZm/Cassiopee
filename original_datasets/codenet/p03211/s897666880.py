S = input()
i = 0
min_dif = 754
while i+2 <= len(S):
    x = int(S[i:i+3])
    if min_dif >= abs(x - 753):
        min_dif = abs(x - 753)
    i += 1
print(min_dif)