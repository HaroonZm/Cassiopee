def read_int():
    return int(input())

def read_int_list():
    return [int(num) for num in input().split()]

def sort_list(lst):
    lst.sort()
    return lst

def max_value(x, y):
    return max(x, y)

def calc_value(x, y, z, t):
    return (x + y) / (z - t + 0.0)

def calculate_loop_max(a, n):
    ans = 0.0
    for i in range(n - 2):
        curr = calc_value(a[n - 1], a[n - 2], a[i + 1], a[i])
        ans = max_value(ans, curr)
    return ans

def calculate_extra_cases(a, n, ans):
    v1 = calc_value(a[n - 1], a[n - 4], a[n - 2], a[n - 3])
    ans = max_value(ans, v1)
    v2 = calc_value(a[n - 3], a[n - 4], a[n - 1], a[n - 2])
    ans = max_value(ans, v2)
    return ans

def format_result(ans):
    return '%.8f' % ans

def main():
    n = read_int()
    a = read_int_list()
    a = sort_list(a)
    ans = calculate_loop_max(a, n)
    ans = calculate_extra_cases(a, n, ans)
    print(format_result(ans))

main()