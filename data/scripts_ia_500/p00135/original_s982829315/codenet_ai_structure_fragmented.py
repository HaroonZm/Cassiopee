def read_test_cases_count():
    return int(input())

def read_time():
    time_str = input()
    return list(map(int, time_str.split(':')))

def calculate_H(h, m):
    part1 = 30 * h
    part2 = m // 2
    base = part1 + part2
    double_base = base * 2
    if (m & 1) == 1:
        double_base += 1
    return double_base

def calculate_M(m):
    base = 6 * m
    double_base = base * 2
    return double_base

def absolute_difference(a, b):
    diff = a - b
    if diff < 0:
        diff = -diff
    return diff

def minimum_difference(a):
    a2 = 720 - a
    if a2 < a:
        return a2
    return a

def determine_status(angle):
    if angle < 60:
        return "alert"
    elif angle >= 180 and angle <= 360:
        return "safe"
    else:
        return "warning"

def process_single_case():
    h, m = read_time()
    H = calculate_H(h, m)
    M = calculate_M(m)
    a = absolute_difference(H, M)
    a = minimum_difference(a)
    status = determine_status(a)
    print(status)

def main():
    t = read_test_cases_count()
    for _ in range(t):
        process_single_case()

main()