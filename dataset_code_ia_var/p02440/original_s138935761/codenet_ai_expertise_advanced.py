from sys import stdin

_ = input()
arr = list(map(int, input().split()))
qn = int(input())
queries = (line.split() for line in stdin)
operations = {
    '0': lambda a, b, c: min(a[b:c]),
    '1': lambda a, b, c: max(a[b:c]),
}

for idx, (com, b, c) in zip(range(qn), queries):
    b, c = int(b), int(c)
    try:
        print(operations[com](arr, b, c))
    except KeyError:
        raise AssertionError