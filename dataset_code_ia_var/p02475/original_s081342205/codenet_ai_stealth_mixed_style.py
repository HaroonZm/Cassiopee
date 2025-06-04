from sys import stdin

def compute_division():
    nums = [int(x) for x in stdin.readline().split()]
    x = abs(nums[0])
    y = abs(nums[1])
    if nums[0]*nums[1]<0:
        modifier = -1
    else:
        modifier = 1
    def quotient(val1, val2): return val1 // val2
    print(modifier * quotient(x, y))

compute_division()