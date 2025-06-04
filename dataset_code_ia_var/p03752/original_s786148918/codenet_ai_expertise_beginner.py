import sys

n, k = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))

min_cost = float('inf')

for mask in range(1 << (n - 1)):
    visible = 0
    current_cost = 0
    max_height = a_list[0]
    for idx in range(n - 1):
        if (mask >> idx) & 1:
            if max_height >= a_list[idx+1]:
                current_cost += max_height - a_list[idx+1] + 1
                max_height += 1
            else:
                max_height = a_list[idx+1]
            visible += 1
        else:
            if max_height < a_list[idx+1]:
                visible += 1
            max_height = max(max_height, a_list[idx+1])
    if visible >= k - 1:
        if current_cost < min_cost:
            min_cost = current_cost

print(min_cost)