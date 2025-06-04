S = list(input())

i = 0
while i < len(S):
    if S[i].isupper():
        S[i] = S[i].lower()
    else:
        S[i] = S[i].upper()
    i += 1

print(''.join(S))