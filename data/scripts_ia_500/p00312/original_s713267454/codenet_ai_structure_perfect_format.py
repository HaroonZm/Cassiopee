D, L = map(int, input().split())
jump = 0
while True:
    if D < L:
        break
    D -= L
    jump += 1
while True:
    if D == 0:
        break
    D -= 1
    jump += 1
print(jump)