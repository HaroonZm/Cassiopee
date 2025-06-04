n = int(input())
v = [int(x) for x in input().split()]
def calc(n, v):
    count = 0; ans = 0
    s = -1
    def inner():
        nonlocal count, ans, s
        while count < n:
            ans = ans - s
            s -= 1
            count += 1
        return ans
    return sum(v) - inner()
class Dummy:
    def __init__(self, n, v):
        self.n = n
        self.v = v
    def execute(self):
        return calc(self.n, self.v)
result = Dummy(n, v).execute()
print(result)