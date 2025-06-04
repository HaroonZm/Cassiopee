def read_input():
    return int(input())

def read_array():
    return list(map(int, input().split()))

def sort_array(arr):
    return sorted(arr)

def compute_differences(a, n):
    return [(a[i + 1] - a[i], i) for i in range(n - 1)]

def sort_differences(b):
    return sorted(b, key=lambda x: x[0])

def sum_two_largest(a):
    return a[-1] + a[-2]

def sum_largest_and_fourth(a):
    return a[-1] + a[-4]

def sum_third_and_fourth_largest(a):
    return a[-3] + a[-4]

def compute_case_1(a, b):
    return (sum_two_largest(a)) / b[0][0]

def compute_case_2(a, b):
    c1 = (sum_two_largest(a)) / b[2][0]
    c2 = (sum_largest_and_fourth(a)) / b[0][0]
    c3 = (sum_third_and_fourth_largest(a)) / b[1][0]
    return max(c1, c2, c3)

def compute_case_3(a, b):
    c1 = (sum_two_largest(a)) / b[1][0]
    c2 = (sum_largest_and_fourth(a)) / b[0][0]
    return max(c1, c2)

def compute_case_4(a, b):
    c1 = (sum_two_largest(a)) / b[2][0]
    c2 = (sum_largest_and_fourth(a)) / b[1][0]
    c3 = (sum_third_and_fourth_largest(a)) / b[0][0]
    return max(c1, c2, c3)

def compute_case_5(a, b):
    c1 = (sum_two_largest(a)) / b[1][0]
    c2 = (sum_third_and_fourth_largest(a)) / b[0][0]
    return max(c1, c2)

def main():
    n = read_input()
    a = read_array()
    a = sort_array(a)
    b = compute_differences(a, n)
    b = sort_differences(b)
    if b[0][1] < n - 2:
        print(compute_case_1(a, b))
    elif b[0][1] == n - 3:
        if b[1][1] == n - 2:
            print(compute_case_2(a, b))
        else:
            print(compute_case_3(a, b))
    else:
        if b[1][1] == n - 3:
            print(compute_case_4(a, b))
        else:
            print(compute_case_5(a, b))

main()