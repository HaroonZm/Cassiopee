from typing import List, Tuple, Dict, Any
import sys
import heapq
import bisect

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Task:
    __slots__ = ['id', 'attributes']
    def __init__(self, id: int, attributes: List[int]):
        self.id = id
        self.attributes = attributes

class DependencyGraph:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[int]] = [[] for _ in range(n + 1)]
        self.in_degree: List[int] = [0] * (n + 1)

    def add_edge(self, frm: int, to: int):
        self.adj[frm].append(to)
        self.in_degree[to] += 1

class EvaluationOrder:
    def __init__(self, order: List[int]):
        self.order = order  # 1-based indices of attribute priority

    def key_func(self, task: Task) -> Tuple:
        # Return tuple for priority heap: negate values for max priority
        # Also add task.id for tie-break determinism
        return tuple(-task.attributes[i - 1] for i in self.order) + (task.id,)

class Scheduler:
    """
    Ultra sophisticated scheduler for UnixGnu15 OS,
    built with extensibility and abstraction in mind.
    """
    def __init__(self, tasks: List[Task], graph: DependencyGraph,
                 initial_eval_order: EvaluationOrder,
                 order_change_points: List[Tuple[int, EvaluationOrder]]):
        self.tasks = tasks
        self.graph = graph
        self.eval_order_changes = order_change_points
        self.eval_order = initial_eval_order

        # Index tasks by id for quick access
        self.task_map: Dict[int, Task] = {t.id: t for t in tasks}

        # Current heap and tracking structures
        self.ready_heap: List[Tuple[Any, int]] = []
        self.executed_count = 0
        self.change_iter = iter(order_change_points)
        self.next_change = next(self.change_iter, None)

    def _push_ready_task(self, task_id: int):
        task = self.task_map[task_id]
        key = self.eval_order.key_func(task)
        heapq.heappush(self.ready_heap, (key, task_id))

    def _update_ready_heap_order(self):
        # When eval_order changes, need to re-heapify
        new_heap = []
        for _, tid in self.ready_heap:
            task = self.task_map[tid]
            key = self.eval_order.key_func(task)
            new_heap.append((key, tid))
        heapq.heapify(new_heap)
        self.ready_heap = new_heap

    def _check_order_change(self):
        # If current executed count matches next change point, update order
        if self.next_change and self.executed_count == self.next_change[0]:
            self.eval_order = self.next_change[1]
            self._update_ready_heap_order()
            self.next_change = next(self.change_iter, None)

    def run(self) -> List[int]:
        # Initialize ready tasks (in_degree == 0)
        for i in range(1, self.graph.n + 1):
            if self.graph.in_degree[i] == 0:
                self._push_ready_task(i)

        execution_order: List[int] = []

        while self.ready_heap:
            self._check_order_change()
            _, tid = heapq.heappop(self.ready_heap)
            execution_order.append(tid)
            self.executed_count += 1

            for nxt in self.graph.adj[tid]:
                self.graph.in_degree[nxt] -= 1
                if self.graph.in_degree[nxt] == 0:
                    self._push_ready_task(nxt)

        return execution_order

class InputParser:
    @staticmethod
    def parse() -> Tuple[List[Task], DependencyGraph, EvaluationOrder, List[Tuple[int, EvaluationOrder]]]:
        N, K = map(int, input().split())
        tasks = []
        for i in range(1, N+1):
            attributes = list(map(int, input().split()))
            tasks.append(Task(i, attributes))

        graph = DependencyGraph(N)
        D = int(input())
        for _ in range(D):
            a, b = map(int, input().split())
            graph.add_edge(a, b)

        initial_order = list(map(int, input().split()))
        initial_eval_order = EvaluationOrder(initial_order)

        R = int(input())
        changes = []
        for _ in range(R):
            data = list(map(int, input().split()))
            m = data[0]
            order = data[1:]
            changes.append((m, EvaluationOrder(order)))

        return tasks, graph, initial_eval_order, changes

def main():
    tasks, graph, initial_eval_order, changes = InputParser.parse()
    scheduler = Scheduler(tasks, graph, initial_eval_order, changes)
    result = scheduler.run()
    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()