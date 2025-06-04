def get_input():
    return input()

def parse_input(s):
    return list(map(int, s.split()))

def check_parity(t, x, y):
    return ((x + y) % 2) == (t % 2)

def check_sum(x, y, t):
    return (x + y) <= t

def evaluate_step(t, x, y):
    if not check_parity(t, x, y):
        return False
    if not check_sum(x, y, t):
        return False
    return True

def process_steps(N):
    flag = 1
    for _ in range(N):
        s = get_input()
        t, x, y = parse_input(s)
        if not evaluate_step(t, x, y):
            flag = 0
    return flag

def print_result(flag):
    if flag:
        print("Yes")
    else:
        print("No")

def main():
    N = int(get_input())
    flag = process_steps(N)
    print_result(flag)

main()