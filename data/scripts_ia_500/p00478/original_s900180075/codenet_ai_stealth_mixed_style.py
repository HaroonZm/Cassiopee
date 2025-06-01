t = input()
n = int(input())
results = []
for _ in range(n):
    s = input()
    results.append(t in s * 2)
print(sum(results))