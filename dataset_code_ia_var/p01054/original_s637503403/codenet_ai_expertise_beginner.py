# AOJ 1568: String Conversion - version débutant

a = input()
S = [0] * 26
for x in a:
    S[ord(x) - ord('a')] += 1

b = input()
T = [0] * 26
for x in b:
    T[ord(x) - ord('a')] += 1

total_diff = 0
for i in range(26):
    total_diff += abs(S[i] - T[i])

print(total_diff // 2)