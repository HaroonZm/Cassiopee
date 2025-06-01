from functools import reduce
class Avg:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def compute(self):
        return reduce(lambda a,b: a+b, self.data, 0)//len(self.data)
n = (lambda s: int(''.join(map(chr, map(lambda x: x+48, [int(i) for i in s])))))(input())
avg = Avg()
list(map(lambda _: avg.add(int(''.join(filter(str.isdigit, input())))), range(n)))
print(avg.compute())