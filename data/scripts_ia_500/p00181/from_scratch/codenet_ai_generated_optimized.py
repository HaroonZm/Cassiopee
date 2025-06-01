import sys
input=sys.stdin.readline

def can_fit(w, m, width):
    count = 1
    current_sum = 0
    for thickness in w:
        if thickness > width:
            return False
        if current_sum + thickness <= width:
            current_sum += thickness
        else:
            count += 1
            current_sum = thickness
            if count > m:
                return False
    return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    w = [int(input()) for _ in range(n)]
    left, right = max(w), sum(w)
    while left < right:
        mid = (left + right) // 2
        if can_fit(w, m, mid):
            right = mid
        else:
            left = mid + 1
    print(left)