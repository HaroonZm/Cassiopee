import itertools

n = int(input())
A = tuple(map(int, input().split()))
q = int(input())
B = tuple(map(int, input().split()))

memo = set()
for i in range(1, n + 1):
    for nums in itertools.combinations(A, i):
        memo.add(sum(nums))

for m in B:
    print('yes' if m in memo else 'no')