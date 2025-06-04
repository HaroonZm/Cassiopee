import sys
from sys import stdin
input = stdin.readline

while True:
    m = int(input())
    if m == 0:
        break
    results = []
    for _ in range(m):
        data = [int(x) for x in input().split()]
        name_id = data[0]
        rolls = data[1:]
        frame = 1
        scores = [0] * 11
        i = 0
        while frame <= 10:
            if rolls[i] == 10:
                scores[frame] = rolls[i] + rolls[i+1] + rolls[i+2]
                i += 1
                frame += 1
            elif rolls[i] + rolls[i+1] == 10:
                scores[frame] = rolls[i] + rolls[i+1] + rolls[i+2]
                i += 2
                frame += 1
            else:
                scores[frame] = rolls[i] + rolls[i+1]
                i += 2
                frame += 1
        total = sum(scores[1:])
        results.append([-total, name_id])
    results.sort()
    for s, i in results:
        print(i, -s)