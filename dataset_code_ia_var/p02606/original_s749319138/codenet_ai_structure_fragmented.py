def inputlist():
    return [int(j) for j in input().split()]

def get_L_R_d():
    vals = inputlist()
    return vals[0], vals[1], vals[2]

def is_divisible(n, d):
    return n % d == 0

def calculate_count(L, R, d):
    count = 0
    for i in range(get_start(L), get_end(R)):
        if check_divisibility(i, d):
            count = increment(count)
    return count

def get_start(L):
    return L

def get_end(R):
    return R + 1

def check_divisibility(i, d):
    return is_divisible(i, d)

def increment(value):
    return value + 1

def display_result(result):
    print(result)

def main():
    L, R, d = get_L_R_d()
    count = calculate_count(L, R, d)
    display_result(count)

main()