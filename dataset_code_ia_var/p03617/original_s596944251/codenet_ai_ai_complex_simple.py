from functools import reduce
from operator import mul

q, h, s, d = map(int, input().split())
n = int(input())

bases = [1, 2, 4, 8]
costs = [q, h, s, d]

def insane_sort(a):
    # Custom sort using tuple: (value, original index)
    return [i for _, i in sorted(zip([8*q, 4*h, 2*s, d], range(4)))]

order = insane_sort(costs)
total_8ths = 4 * n
result = 0

class Weird:
    def __init__(self, indices, bases, costs):
        self.indices = indices
        self.bases = bases
        self.costs = costs
        self.memo = {}

    def decompose(self, value):
        return [(value // self.bases[i], value % self.bases[i]) for i in self.indices]

    def next_val(self, rem, idx):
        use = rem // self.bases[idx]
        return use, rem - use * self.bases[idx]

    def accumulate(self, all_total):
        rest = all_total
        res = 0
        for idx in self.indices:
            use, rest = self.next_val(rest, idx)
            res += self.costs[idx] * use
        return res

result = Weird(order, bases, costs).accumulate(total_8ths)
print(result)