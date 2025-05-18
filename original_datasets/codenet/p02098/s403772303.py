t1 = int(input())
t2 = int(input())
if not t1 < t2:
    t1, t2 = t2, t1
if t2 - t1 <= 180:
    print((t2 + t1)/2)
else:
    print(((t2 + t1 + 360) % 720)/2)