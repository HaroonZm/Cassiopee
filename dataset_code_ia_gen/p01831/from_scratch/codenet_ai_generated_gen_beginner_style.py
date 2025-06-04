N = int(input())
S = input()

max_removed = 0

for start in range(N):
    panels = list(S)
    pos = start
    direction = 0  # 0 means initial, will be set to arrow direction
    removed = 0
    while 0 <= pos < len(panels):
        direction = 1 if panels[pos] == '>' else -1
        # remove current panel
        panels.pop(pos)
        removed += 1
        # move in current direction until find next panel
        # since panels list shrinks, just move by direction steps
        pos += direction
        # if out of range, break
        if pos < 0 or pos >= len(panels):
            break
    if removed > max_removed:
        max_removed = removed

print(max_removed)