w, h, x, y, r = eval(input().replace(' ', ','))
print("Yes" if r <= x <= w - r and r <= y <= h - r else "No")