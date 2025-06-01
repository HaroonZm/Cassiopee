class Graph():
    from collections import namedtuple
    __Pair = namedtuple("Pair", "cost point")

    def __init__(self, element_count):
        self.__element_count = element_count
        self.__adjacency_iist = [[] for _ in range(element_count)]

    def get_path(self, begin_Point, end_point, cost):
        item = self.__Pair(cost, end_point)
        self.__adjacency_iist[begin_Point].append(item)

    def dijkstra(self, begin_Point):
        from sys import maxsize as MAX_VALUE
        from queue import PriorityQueue
        state_table = {"NotVisited": 0, "Stay": 1, "Visited": 2}
        pq = PriorityQueue()
        cost_table = [MAX_VALUE for _ in range(self.__element_count)]
        visit_state = [state_table["NotVisited"] for _ in range(self.__element_count)]
        cost_table[begin_Point] = 0
        pq.put_nowait(self.__Pair(0, begin_Point))
        while not pq.empty():
            min_item = pq.get_nowait()
            min_point, min_cost = min_item.point, min_item.cost
            visit_state[min_point] = state_table["Visited"]
            if min_cost <= cost_table[min_point]:
                for cost, point in self.__adjacency_iist[min_point]:
                    if visit_state[point] != state_table["Visited"]:
                        if cost_table[min_point] + cost < cost_table[point]:
                            cost_table[point] = cost_table[min_point] + cost
                            visit_state[point] = state_table["Stay"]
                            pq.put_nowait(self.__Pair(cost_table[point], point))
        return cost_table

router_count = int(input())
graph = Graph(router_count)
for _ in range(router_count):
    data = [int(item) for item in input().split(" ")]
    data[0] -= 1
    for lp in range(data[1]):
        graph.get_path(data[0], data[2 + lp] - 1, 1)
for _ in range(int(input())):
    sender, destination, ttl = [int(item) for item in input().split(" ")]
    costs = graph.dijkstra(sender - 1)
    cost = costs[destination - 1] + 1
    if cost <= ttl:
        print(cost)
    else:
        print("NA")