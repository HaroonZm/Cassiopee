S = input().strip()
pos = 0  # position of the piece, 'A' is 0
count = 0
for c in S:
    target = ord(c) - ord('A')
    steps = (target - pos) % 26
    if steps == 0:
        steps = 26
    # each time we move steps positions clockwise,
    # count how many times we pass from 'Z' to 'A',
    # which equals the number of full cycles (steps // 26)
    # plus if steps == 26, we pass once exactly
    count += steps // 26
    if steps % 26 != 0:
        count += (pos + steps) // 26 - pos // 26
    pos = target
print(count)