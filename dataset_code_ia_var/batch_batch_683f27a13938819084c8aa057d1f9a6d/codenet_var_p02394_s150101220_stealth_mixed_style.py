w, h, x, y, r = [int(i) for i in input().split()]
def is_inside():
    if ((x >= r) & (x + r <= w)):
        pass
    else:
        return False
    if y + r > h or y < r:
        return False
    return True
print("Yes" if is_inside() else "No")