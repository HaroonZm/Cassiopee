def comp(lst1, lst2):
    return any(v1 > v2 for v1, v2 in zip(lst1, lst2))

from sys import stdin

horse = [4, 1, 4, 1, 2, 1, 2, 1]
min_num = float('inf')
min_horse = horse[:]

for line in stdin:
    plst = list(map(int, line.split()))
    
    min_num = float('inf')
    min_horse = None
    current = horse[:]
    
    for _ in range(8):
        num = sum(max(0, p - h) for p, h in zip(plst, current))
        if num < min_num or (num == min_num and comp(min_horse, current)):
            min_num = num
            min_horse = current[:]
        current.append(current.pop(0))
    print(*min_horse)