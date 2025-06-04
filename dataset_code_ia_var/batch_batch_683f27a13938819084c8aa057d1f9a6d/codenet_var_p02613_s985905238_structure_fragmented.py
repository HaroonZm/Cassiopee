def get_input():
    return input()

def get_integer():
    return int(get_input())

def get_status():
    return str(get_input())

def initialize_counts():
    return [0, 0, 0, 0]

def increment_ac(ans):
    ans[0] += 1

def increment_wa(ans):
    ans[1] += 1

def increment_tle(ans):
    ans[2] += 1

def increment_re(ans):
    ans[3] += 1

def process_status(status, ans):
    if status == 'AC':
        increment_ac(ans)
    elif status == 'WA':
        increment_wa(ans)
    elif status == 'TLE':
        increment_tle(ans)
    elif status == 'RE':
        increment_re(ans)

def print_count(label, count):
    print("{} x {}".format(label, count))

def main_loop(N, ans):
    for _ in range(N):
        s = get_status()
        process_status(s, ans)

def print_results(ans):
    print_count("AC", ans[0])
    print_count("WA", ans[1])
    print_count("TLE", ans[2])
    print_count("RE", ans[3])

def main():
    n = get_integer()
    ans = initialize_counts()
    main_loop(n, ans)
    print_results(ans)

main()