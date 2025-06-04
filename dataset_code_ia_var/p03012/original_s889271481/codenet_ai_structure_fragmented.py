def get_input():
    return int(input())

def get_nlist():
    return list(map(int, input().split()))

def prefix_slice(lst, idx):
    return lst[:idx+1]

def suffix_slice(lst, idx):
    return lst[idx+1:]

def calc_sum(lst):
    return sum(lst)

def calc_abs_diff(left_sum, right_sum):
    return abs(left_sum - right_sum)

def calc_partition_abs(lst, idx):
    left = prefix_slice(lst, idx)
    right = suffix_slice(lst, idx)
    left_sum = calc_sum(left)
    right_sum = calc_sum(right)
    return calc_abs_diff(left_sum, right_sum)

def build_abslist(lst, n):
    abslist = []
    for i in range(n-1):
        abs_val = calc_partition_abs(lst, i)
        abslist.append(abs_val)
    return abslist

def get_min(lst):
    return min(lst)

def main():
    n = get_input()
    nlist = get_nlist()
    abslist = build_abslist(nlist, n)
    min_val = get_min(abslist)
    print(min_val)

main()