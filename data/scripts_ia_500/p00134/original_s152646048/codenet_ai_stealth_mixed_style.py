n = int(input())
prices = list(map(int, (input() for _ in range(n))))

def average(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total // len(nums)

class Result:
    def __init__(self, value):
        self.value = value
    def display(self):
        print(self.value)

ans = average(prices)
res = Result(ans)
res.display()