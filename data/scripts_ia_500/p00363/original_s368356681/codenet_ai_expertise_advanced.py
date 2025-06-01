w, h, c = input().split()
w, h = map(int, (w, h))

mid_w = w // 2 + 1
mid_h = h // 2 + 1

top_bottom = f"+{'-' * (w - 2)}+"

for y in range(h):
    if y == 0 or y == h - 1:
        print(top_bottom)
    else:
        if y == mid_h:
            middle = ''.join(c if x == mid_w else '.' for x in range(1, w - 1))
        else:
            middle = '.' * (w - 2)
        print(f"|{middle}|")