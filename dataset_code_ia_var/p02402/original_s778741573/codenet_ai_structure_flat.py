n = int(input())
a = list(map(int, input().split()))
a_min = sorted(a)
a_sum = 0
for x in a:
    a_sum += x
print(a_min[0], a_min[-1], a_sum)