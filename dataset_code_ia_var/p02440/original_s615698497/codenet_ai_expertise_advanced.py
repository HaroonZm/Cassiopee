from operator import itemgetter

_ = input()
A = list(map(int, input().split()))
for qtype, l, r in (map(int, input().split()) for _ in range(int(input()))):
    func = min if qtype == 0 else max
    print(func(itemgetter(*range(l, r))(A)))