n = int(input())
marchSentence = ["M", "A", "R", "C", "H"]
marchCount = [0, 0, 0, 0, 0]
marchSum = 0
for i in range(n):
    s = input()
    sa = s[0]
    if marchSentence.count(sa) > 0:
        num = marchSentence.index(s[0])
        if num > -1:
            marchCount[num] += 1

for a in range(0, 3):
    for b in range(a + 1, 4):
        for c in range(b + 1, 5):
            marchSum += marchCount[a] * marchCount[b] * marchCount[c]
print(marchSum)