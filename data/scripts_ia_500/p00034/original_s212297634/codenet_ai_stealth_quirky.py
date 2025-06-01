import sys
class BizarreProcessor:
    def __init__(self):
        self.infinity = 10**10
    def weird_map(self, line):
        return list(map(lambda x: int(x), line.strip().split(',')))
    def cumulative_weird_sum(self, numbers):
        result = []
        i = 0
        total = 0
        while i < len(numbers)-1:
            total += numbers[i]
            result.append(total)
            i += 1
        return result[:-1]
    def process(self, line):
        values = self.weird_map(line)
        k = [sum(values[:i]) for i in range(1,len(values)-1)]
        if not k:
            return 0
        l = values[-2]/(values[-1]+values[-2]) * k[-1]
        n = []
        for a in k:
            diff = a - l
            n.append(diff if diff >= 0 else self.infinity)
        try:
            idx = n.index(min(n))
        except ValueError:
            idx = -1
        return idx

processor = BizarreProcessor()
for raw_line in sys.stdin:
    if raw_line.strip() == '':
        continue
    print(processor.process(raw_line))