def read_integer():
    return int(input())

def read_position():
    return list(map(int, input().split()))

def adjust_coordinate(coord, n):
    if coord > n // 2:
        return n - coord + 1
    return coord

def adjust_position(pos, n):
    x_adjusted = adjust_coordinate(pos[0], n)
    y_adjusted = adjust_coordinate(pos[1], n)
    return x_adjusted, y_adjusted

def calculate_color_equal(x):
    return ((x - 1) % 3) + 1

def calculate_color_min(min_val):
    return ((min_val - 1) % 3) + 1

def solve(n, pos):
    x, y = adjust_position(pos, n)
    if x == y:
        color = calculate_color_equal(x)
    else:
        definitive = min(x, y)
        color = calculate_color_min(definitive)
    return color

def main():
    n = read_integer()
    k = read_integer()
    for _ in range(k):
        pos = read_position()
        color = solve(n, pos)
        print(color)

main()