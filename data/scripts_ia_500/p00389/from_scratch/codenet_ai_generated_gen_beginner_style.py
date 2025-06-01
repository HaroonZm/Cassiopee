N, K = map(int, input().split())

height = 0  # nombre d'étages
used = 0    # nombre de blocs utilisés

while True:
    next_stage = height + 1
    if used + next_stage > N:
        break
    if next_stage > K:
        break
    used += next_stage
    height += 1

print(height)