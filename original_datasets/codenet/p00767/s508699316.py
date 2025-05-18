def main(h,w):
    a = h * h + w * w
    ans = []
    for x in range(1,151):
        for y in range(x+1,151):
            if a <= x ** 2 + y ** 2:
                b = x ** 2 + y ** 2
                ans.append((b, x, y))
    ans.sort()
    for b, x, y in ans:
        if a < b or x > h:
            ans = [x, y]
            break
    print(" ".join(list(map(str,ans))))
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    main(h,w)