from bisect import bisect_right

rectangles = [(h ** 2 + w ** 2, h, w) for h in range(1, 151) for w in range(1, 151) if h < w]
rectangles.sort()

while True:
    h, w = map(int, input().split())
    if not h and not w:
        break

    gt_rectangle = rectangles[bisect_right(rectangles, (h ** 2 + w ** 2, h, w))]
    print(gt_rectangle[1], gt_rectangle[2])