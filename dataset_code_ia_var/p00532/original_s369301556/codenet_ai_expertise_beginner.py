n = int(input())
results = []
for i in range(n):
    results.append(0)
m = int(input())
a = input().split()
a = [int(x) for x in a]

for k in range(m):
    target = a[k]
    result = input().split()
    result = [int(x) for x in result]
    for idx in range(len(result)):
        if result[idx] == target:
            results[idx] = results[idx] + 1
    count_target = 0
    for rr in result:
        if rr == target:
            count_target = count_target + 1
    results[target - 1] = results[target - 1] + (len(results) - count_target)

for r in results:
    print(r)