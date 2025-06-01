while True:
    n = int(input())
    if not n:
        break
    y = int(input())
    z = []
    max_gain = -float('inf')
    chosen_num = None
    for _ in range(n):
        z += [list(map(int, input().split()))]
    for item in z:
        idx, rate, typ = item
        gain = (1 + rate/100*y) if typ == 1 else (1 + rate/100) ** y if typ == 2 else 0
        if gain > max_gain:
            max_gain, chosen_num = gain, idx
    print(chosen_num)