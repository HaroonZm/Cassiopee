def read_input():
    return map(int, input().split())

def read_floor(n):
    floor = []
    for _ in range(n):
        floor.append(list(input()))
    return floor

def is_within_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def is_dot(cell):
    return cell == "."

def test_horizontal(floor, i, j, m, d):
    for k in range(1, d):
        if not is_within_bounds(i, j + k, len(floor), m):
            return False
        if not is_dot(floor[i][j + k]):
            return False
    return True

def test_vertical(floor, i, j, n, d):
    for k in range(1, d):
        if not is_within_bounds(i + k, j, n, len(floor[0])):
            return False
        if not is_dot(floor[i + k][j]):
            return False
    return True

def process_cell(floor, i, j, n, m, d):
    count = 0
    if is_dot(floor[i][j]):
        if d > 1 and test_horizontal(floor, i, j, m, d):
            count += 1
        if d > 1 and test_vertical(floor, i, j, n, d):
            count += 1
    return count

def count_positions(floor, n, m, d):
    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += process_cell(floor, i, j, n, m, d)
    return cnt

def main():
    n, m, d = read_input()
    floor = read_floor(n)
    if d == 1:
        print(sum(row.count('.') for row in floor))
    else:
        cnt = count_positions(floor, n, m, d)
        print(cnt)

main()