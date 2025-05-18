import heapq

def Main():
    N, capacity = map(int, input().split())
    w_list = list()

    for _ in range(N):
        v, w = map(int, input().split())
        heapq.heappush(w_list, [-1*float(v/w), v, w] )

    total_value = 0

    while len(w_list) != 0:
        item = heapq.heappop(w_list)
        value_per_weight = -1*item[0]
        value = item[1]
        weight = item[2]
        
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += capacity * value_per_weight
            break
        
    print(total_value)

Main()