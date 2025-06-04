def can_divide(widths, m, max_width):
    current_sum = 0
    shelves_used = 1
    for w in widths:
        if w > max_width:
            return False
        if current_sum + w <= max_width:
            current_sum += w
        else:
            shelves_used += 1
            current_sum = w
            if shelves_used > m:
                return False
    return True

while True:
    line = input().strip()
    if not line:
        continue
    m, n = map(int, line.split())
    if m == 0 and n == 0:
        break
    widths = [int(input()) for _ in range(n)]

    left, right = max(widths), 1500000
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_divide(widths, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(result)