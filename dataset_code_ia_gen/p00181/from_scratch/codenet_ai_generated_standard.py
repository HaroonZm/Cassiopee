import sys

def can_place(w, m, widths, max_width):
    count = 1
    current_sum = 0
    for width in widths:
        if width > max_width:
            return False
        if current_sum + width <= max_width:
            current_sum += width
        else:
            count += 1
            current_sum = width
            if count > m:
                return False
    return True

for line in sys.stdin:
    if not line.strip():
        continue
    m, n = map(int, line.split())
    if m == 0 and n == 0:
        break
    widths = [int(sys.stdin.readline()) for _ in range(n)]
    left, right = max(widths), sum(widths)
    while left < right:
        mid = (left + right) // 2
        if can_place(m, n, widths, mid):
            right = mid
        else:
            left = mid + 1
    print(left)