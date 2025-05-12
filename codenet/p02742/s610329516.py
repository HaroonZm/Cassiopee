h, w = map(int, input().split())

if w == 1 or h == 1:
    print(1)
elif h%2 == 0:
    print(w * (h//2))
else:
    print(w * (h//2) + int(w/2+.5))