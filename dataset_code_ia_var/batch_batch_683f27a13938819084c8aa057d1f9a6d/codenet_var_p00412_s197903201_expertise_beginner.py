num_lane, num_info = map(int, input().split())
Q = []
for i in range(num_lane):
    Q.append([])  # on va utiliser une liste au lieu de deque pour simplifier

for i in range(num_info):
    command, value = map(int, input().split())
    if command == 0:
        value = value - 1
        print(Q[value][0])
        Q[value].pop(0)
    else:
        min_cars = 1000000000
        min_lane = 0
        for j in range(num_lane):
            if len(Q[j]) < min_cars:
                min_cars = len(Q[j])
                min_lane = j
        Q[min_lane].append(value)