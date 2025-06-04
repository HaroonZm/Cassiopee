def can_fit(width, shelves, books):
    count = 1
    current_width = 0
    for w in books:
        if w > width:
            return False
        if current_width + w <= width:
            current_width += w
        else:
            count += 1
            current_width = w
            if count > shelves:
                return False
    return True

while True:
    line = input().strip()
    if not line:
        continue
    m, n = map(int, line.split())
    if m == 0 and n == 0:
        break
    books = [int(input()) for _ in range(n)]
    left = max(books)
    right = 1500000
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_fit(mid, m, books):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)