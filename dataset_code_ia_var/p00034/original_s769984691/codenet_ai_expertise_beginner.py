import sys

def d(o):
    m = o[-2] / sum(o[-2:])
    l = sum(o[:-2])
    def p(x):
        return sum(o[:x]) / l
    for i in range(1, len(o) - 1):
        if p(i) >= m:
            return i

lists = []
for line in sys.stdin:
    numbers = line.strip().split(",")
    numbers = [int(n) for n in numbers]
    lists.append(numbers)

results = []
for o in lists:
    result = d(o)
    results.append(result)

for i in results:
    print(i)