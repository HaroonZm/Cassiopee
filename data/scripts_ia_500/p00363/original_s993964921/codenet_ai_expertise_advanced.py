W, H, c = map(str.strip, input().split())
W, H = map(int, (W, H))
mid = ((W - 1) // 2, (H - 1) // 2)
corners = {(0, 0), (0, H - 1), (W - 1, 0), (W - 1, H - 1)}

print('\n'.join(
    ''.join(
        '+' if (x, y) in corners else
        '|' if x in {0, W - 1} else
        '-' if y in {0, H - 1} else
        c if (x, y) == mid else
        '.'
        for x in range(W)
    ) for y in range(H)
))