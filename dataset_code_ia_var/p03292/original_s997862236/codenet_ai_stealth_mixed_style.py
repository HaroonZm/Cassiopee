nums = [int(x) for x in input().split()]
def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

sorted_nums = custom_sort(nums)
def compute_difference(arr):
    return arr[-1] - arr[0]
print(compute_difference(sorted_nums))