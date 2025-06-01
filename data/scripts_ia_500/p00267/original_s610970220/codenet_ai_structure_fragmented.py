import sys

def read_input():
    return sys.stdin.readline().strip()

def convert_to_int_list(line):
    return list(map(int, line.split()))

def double_elements(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    return result

def double_elements_plus_one(lst):
    result = []
    for num in lst:
        result.append(num * 2 + 1)
    return result

def combine_and_sort_desc(list1, list2):
    combined = []
    for num in list1:
        combined.append(num)
    for num in list2:
        combined.append(num)
    combined.sort(reverse=True)
    return combined

def update_counters(num, cnt1, cnt2):
    if num % 2 == 1:
        cnt2 += 1
    else:
        cnt1 += 1
    return cnt1, cnt2

def condition_met(cnt1, cnt2, N):
    if (cnt1 - cnt2) * 2 > cnt1 and cnt1 != N:
        return True
    return False

def process_list(ls, N):
    cnt1 = 0
    cnt2 = 0
    ans = "NA"
    for num in ls:
        cnt1, cnt2 = update_counters(num, cnt1, cnt2)
        if num % 2 == 0:
            if condition_met(cnt1, cnt2, N):
                ans = cnt1
                break
    return ans

def main_loop():
    while True:
        N_str = read_input()
        if N_str == '0' or N_str == 0:
            break
        N = int(N_str)
        a_line = read_input()
        b_line = read_input()
        a_list = convert_to_int_list(a_line)
        b_list = convert_to_int_list(b_line)
        double_a = double_elements(a_list)
        double_b = double_elements_plus_one(b_list)
        combined_list = combine_and_sort_desc(double_a, double_b)
        result = process_list(combined_list, N)
        print(result)

main_loop()