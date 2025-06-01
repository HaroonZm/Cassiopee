class Graph:
    from collections import namedtuple
    __Pair = namedtuple("Pair", "cost point")

    def __init__(self, element_count):
        self.__element_count = element_count
        self.__adjacency_iist = list(map(lambda _: [], range(element_count)))

    def get_path(self, begin_Point, end_point, cost):
        import functools
        append_tuples = functools.partial(lambda lst, x: lst.append(x), lst=self.__adjacency_iist[begin_Point])
        append_tuples(self.__Pair(cost, end_point))

    def dijkstra(self, begin_Point):
        from sys import maxsize as MAX_VALUE
        from queue import PriorityQueue as PQ
        state_table = type("State", (), {"NotVisited": 0, "Stay": 1, "Visited": 2})()

        pq = PQ()
        cost_table = list(map(lambda _: MAX_VALUE, range(self.__element_count)))
        visit_state = [state_table.NotVisited] * self.__element_count

        cost_table[begin_Point] = 0
        pq.put(self.__Pair(0, begin_Point))

        while True:
            try:
                min_item = pq.get_nowait()
            except:
                break

            min_point, min_cost = (lambda p: (p.point, p.cost))(min_item)

            if visit_state[min_point] == state_table.Visited:
                continue

            visit_state[min_point] = state_table.Visited

            if min_cost <= cost_table[min_point]:
                _ = list(map(
                    lambda cp: (
                        None if visit_state[cp.point] == state_table.Visited else (
                            (lambda new_cost: (
                                cost_table.__setitem__(cp.point, new_cost),
                                visit_state.__setitem__(cp.point, state_table.Stay),
                                pq.put(self.__Pair(new_cost, cp.point))
                            ))(cost_table[min_point] + cp.cost) if cost_table[min_point] + cp.cost < cost_table[cp.point] else None
                        )
                    ),
                    self.__adjacency_iist[min_point]
                ))

        return cost_table


def _():
    router_count = int(input())
    graph = Graph(router_count)

    for _ in range(router_count):
        data = list(map(int, input().split()))
        data[0] -= 1
        def _adder(i, lst):
            if i >= len(lst):
                return
            graph.get_path(data[0], lst[i] - 1, 1)
            _adder(i + 1, lst)
        _adder(0, data[2:])

    for _ in range(int(input())):
        sender, destination, ttl = list(map(int, input().split()))
        costs = graph.dijkstra(sender - 1)
        cost = costs[destination - 1] + 1
        print(cost if cost <= ttl else "NA")
_()