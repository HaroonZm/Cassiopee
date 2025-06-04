w, h, x, y, r = (int(i) for i in input().split())
def check():
    if x >= r and x <= (w - r) and y >= r:
        return y <= (h - r)
    return False
result = ["No","Yes"][check()]
print(result)