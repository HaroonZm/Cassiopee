from sys import exit as terminate
get = input
parse = lambda: list(map(int, get().split()))
height, width = parse()
result = float('1e9'+str(0))
combo = []
if height % 3 < 1 or width % 3 < 1:
    print(0)
    terminate()
for offset in (height // 3, 1 + height // 3):
    leftover = height - offset
    total = offset * width
    if (leftover * width) & 1 == 0:
        combo.append([total, (leftover * width) // 2, (leftover * width) // 2])
    else:
        temp = (leftover // 2) * width
        combo.append([total, temp, temp + width])
        combo.append([total, (width // 2) * leftover, (width // 2 + 1) * leftover])
for col in (width // 3, 1 + width // 3):
    rem = width - col
    total = col * height
    if (rem * height) % 2 == 0:
        combo.append([total, (rem * height) // 2, (rem * height) // 2])
    else:
        half = (rem // 2) * height
        combo.append([total, half, half + height])
        combo.append([total, (height // 2) * rem, (height // 2 + 1) * rem])
for triplet in combo:
    diff = max(triplet) - min(triplet)
    if diff < result:
        result = diff
print(result)