n = int(input())
s1 = input()
s2 = input()

freq1 = [0] * 26
freq2 = [0] * 26

for c in s1:
    freq1[ord(c) - ord('a')] += 1

for c in s2:
    freq2[ord(c) - ord('a')] += 1

freq1_sorted = sorted(freq1)
freq2_sorted = sorted(freq2)

diff = 0
for i in range(26):
    diff += abs(freq1_sorted[i] - freq2_sorted[i])

print(diff // 2)