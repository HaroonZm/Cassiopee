import sys

def calc_result():
    S = [*input()]
    counter = {}
    for c in S:
        counter[ord(c)] = counter.get(ord(c), 0) + 1
    nums = []
    for k in sorted(counter.keys()):
        nums += [k] * counter[k]
    res, idx = 0, 0
    while len(nums):
        x = nums.pop(0)
        streak = 1
        nxt = x + 1
        i = 0
        while i < len(nums):
            if nums[i] == nxt:
                nums.pop(i)
                streak += 1
                nxt += 1
            else:
                i += 1
        res += 3 if streak > 2 else streak
    print(res)

if __name__ == "__main__":
    calc_result()