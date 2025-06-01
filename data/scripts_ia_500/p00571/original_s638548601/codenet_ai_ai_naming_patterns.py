import sys
sys.setrecursionlimit(2000000000)
read_line = lambda : sys.stdin.readline().rstrip('\n')

num_points = int(read_line())
points_list = []
prefix_sums = [0]

for _index in range(num_points):
    points_list.append(tuple(map(int, read_line().split())))
points_list = [(0, 0)] + sorted(points_list)

for index in range(num_points):
    prefix_sums.append(prefix_sums[-1] + points_list[index + 1][1])

max_difference = 0
current_max = 0
minimum_value = 10**18

for idx in range(1, num_points + 1):
    if minimum_value > prefix_sums[idx - 1] - points_list[idx][0]:
        minimum_value = prefix_sums[idx - 1] - points_list[idx][0]
    if current_max < prefix_sums[idx] - points_list[idx][0] - minimum_value:
        current_max = prefix_sums[idx] - points_list[idx][0] - minimum_value

print(current_max)