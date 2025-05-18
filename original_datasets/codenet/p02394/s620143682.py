w, h, x, y, r = eval(input().replace(' ', ','))
print("Yes" if 0 + r <= x <= w - r and 0 + r <= y <= h - r else "No")