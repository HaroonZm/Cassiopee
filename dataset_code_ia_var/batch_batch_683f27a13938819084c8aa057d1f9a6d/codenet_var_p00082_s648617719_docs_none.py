def comp(lst1, lst2):
    for v1, v2 in zip(lst1, lst2):
        if v1 < v2:
            return False
        if v1 > v2:
            return True
    return False

while True:
    try:
        plst = list(map(int, input().split()))
        horse = [4, 1, 4, 1, 2, 1, 2, 1]
        min_num = 100000
        min_horse = horse[:]
        for _ in range(8):
            num = sum([max(0, plst[j] - horse[j]) for j in range(8)])
            if num == min_num and comp(min_horse, horse):
                min_horse = horse[:]
            elif num < min_num:
                min_num = num
                min_horse = horse[:]
            horse.append(horse.pop(0))
        print(" ".join(map(str, min_horse)))
    except EOFError:
        break