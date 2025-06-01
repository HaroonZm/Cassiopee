def read_dimensions():
    return map(int, input().split())

def read_flag(n):
    flag = []
    for _ in range(n):
        row = list(input())
        flag.append(row)
    return flag

def count_mismatches(flag, start_row, num_rows, color):
    count = 0
    for i in range(start_row, start_row + num_rows):
        for cell in flag[i]:
            if cell != color:
                count += 1
    return count

def calculate_cost(flag, white, blue, n, m):
    red = n - white - blue
    if red <= 0:
        return None
    white_mismatches = count_mismatches(flag, 0, white, "W")
    blue_mismatches = count_mismatches(flag, white, blue, "B")
    red_mismatches = count_mismatches(flag, white + blue, red, "R")
    return white_mismatches + blue_mismatches + red_mismatches

def find_minimum_cost(flag, n, m):
    ans = 10**9
    for white in range(1, n-1):
        for blue in range(1, n-1):
            cost = calculate_cost(flag, white, blue, n, m)
            if cost is not None and cost < ans:
                ans = cost
    return ans

def main():
    n, m = read_dimensions()
    flag = read_flag(n)
    ans = find_minimum_cost(flag, n, m)
    print(ans)

main()