import sys

while True:
    line = sys.stdin.readline()
    nums = line.split()
    total = 0
    for num in nums:
        total += int(num)
    if total == 0:
        break
    scores = [total]
    for i in range(4):
        line = sys.stdin.readline()
        nums = line.split()
        s = 0
        for num in nums:
            s += int(num)
        scores.append(s)
    letters = ['A', 'B', 'C', 'D', 'E']
    max_score = scores[0]
    max_letter = letters[0]
    for i in range(5):
        if scores[i] > max_score:
            max_score = scores[i]
            max_letter = letters[i]
    print(max_letter, max_score)