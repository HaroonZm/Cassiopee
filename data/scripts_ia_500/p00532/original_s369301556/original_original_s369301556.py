results = [0] * int(input())
m = int(input())
a = list(map(int, input().split()))

for i in range(m):
    target = a[i]
    result = list(map(int, input().split()))
    for i, r in enumerate(result):
        if r == target:
            results[i] += 1
    results[target-1] += len(results) - result.count(target)

print(*results, sep="\n")