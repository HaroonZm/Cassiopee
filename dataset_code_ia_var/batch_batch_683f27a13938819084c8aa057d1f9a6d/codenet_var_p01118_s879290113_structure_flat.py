import sys

while True:
    h_w = input()
    h, w = map(int, h_w.split())
    if h == 0 and w == 0:
        break

    keyboard = dict()
    y = 0
    while y < h:
        row = input()
        x = 0
        for ch in row:
            keyboard[ch] = (x, y)
            x += 1
        y += 1

    cx = 0
    cy = 0
    ans = 0
    s = input()
    for ch in s:
        nx, ny = keyboard[ch]
        ans += abs(nx - cx) + abs(ny - cy) + 1
        cx, cy = nx, ny
    print(ans)