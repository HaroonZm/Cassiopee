from collections import defaultdict
N, M = map(int, input().split())
city_road_nums = defaultdict(int)

for _ in range(M):
    a, b = map(int, input().split())
    city_road_nums[a] += 1
    city_road_nums[b] += 1

for i in range(1, N+1):
    print(city_road_nums[i])