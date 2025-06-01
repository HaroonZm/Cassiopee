from typing import List, Tuple, Dict, Callable, Any
import sys
import heapq

sys.setrecursionlimit(10**7)

class Task:
    __slots__ = ('id', 'attributes', 'in_degree', 'dependents')

    def __init__(self, id_: int, attributes: Tuple[int,...]) -> None:
        self.id = id_
        self.attributes = attributes  # Tuple[int,...], indexed 0-based for K attributes
        self.in_degree = 0
        self.dependents: List[int] = []

class EvaluationOrder:
    def __init__(self, order: List[int]) -> None:
        # order holds indexes of attributes in priority order, zero-based
        self.order = order

    def key_func(self, task: Task) -> Tuple:
        # Return a tuple whose natural order represents the task priority:
        # We want max by attributes in order, so use negative values to apply min-heap
        # tasks will be ordered by (-attr[order[0]], -attr[order[1]], ...)
        return tuple(-task.attributes[i] for i in self.order)

    def update_order(self, new_order: List[int]) -> None:
        self.order = new_order

class Scheduler:
    def __init__(self,
                 N: int,
                 K: int,
                 tasks_attributes: List[Tuple[int,...]],
                 dependencies: List[Tuple[int,int]],
                 initial_eval_order: List[int],
                 eval_order_changes: List[Tuple[int, List[int]]]) -> None:
        self.N = N
        self.K = K
        # Instantiate tasks: IDs 1..N mapping to Task objects
        self.tasks: Dict[int, Task] = {
            i+1: Task(i+1, tasks_attributes[i]) for i in range(N)
        }
        # Build graph
        for (a, b) in dependencies:
            self.tasks[a].dependents.append(b)
            self.tasks[b].in_degree += 1
        # Evaluation orders management
        # Convert 1-based to 0-based for attributes indices
        self.eval_order = EvaluationOrder([x-1 for x in initial_eval_order])
        # Sort eval_order_changes by m_i (task count after which order changes)
        self.eval_order_changes = eval_order_changes
        # Index for current change event
        self.eval_order_change_idx = 0
        # Data structures for scheduling
        self.ready_heap: List[Tuple[Any,int]] = []
        self.finished_count = 0
        self.execution_order: List[int] = []

    def run(self) -> List[int]:
        # Initialize ready queue with tasks having zero in-degree
        for task in self.tasks.values():
            if task.in_degree == 0:
                heapq.heappush(self.ready_heap, (self.eval_order.key_func(task), task.id))

        # As we finish tasks, maybe update evaluation order if condition met
        while self.ready_heap:
            # Apply evaluation order changes if necessary
            while (self.eval_order_change_idx < len(self.eval_order_changes) and
                   self.finished_count == self.eval_order_changes[self.eval_order_change_idx][0]):
                _, new_order = self.eval_order_changes[self.eval_order_change_idx]
                # zero-based new_order
                self.eval_order.update_order([x-1 for x in new_order])
                # After changing evaluation order, rebuild heap keys
                self._rebuild_heap()
                self.eval_order_change_idx += 1

            # Pick next task by priority
            _, task_id = heapq.heappop(self.ready_heap)
            self.execution_order.append(task_id)
            self.finished_count += 1

            # Decrement in-degree of dependent tasks
            for nxt_id in self.tasks[task_id].dependents:
                self.tasks[nxt_id].in_degree -= 1
                if self.tasks[nxt_id].in_degree == 0:
                    heapq.heappush(self.ready_heap, (self.eval_order.key_func(self.tasks[nxt_id]), nxt_id))

        return self.execution_order

    def _rebuild_heap(self) -> None:
        # Rebuild the heap keys according to the current evaluation order
        new_heap = []
        for _, tid in self.ready_heap:
            task = self.tasks[tid]
            new_heap.append((self.eval_order.key_func(task), tid))
        heapq.heapify(new_heap)
        self.ready_heap = new_heap


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    tasks_attributes = []
    for _ in range(N):
        attr = tuple(map(int, input().split()))
        tasks_attributes.append(attr)

    D = int(input())
    dependencies = []
    for _ in range(D):
        a, b = map(int, input().split())
        dependencies.append((a,b))

    initial_eval_order = list(map(int, input().split()))

    R = int(input())
    eval_order_changes = []
    for _ in range(R):
        line = input().split()
        m = int(line[0])
        new_order = list(map(int,line[1:1+K]))
        eval_order_changes.append((m,new_order))

    scheduler = Scheduler(N, K, tasks_attributes, dependencies, initial_eval_order, eval_order_changes)
    order = scheduler.run()
    print('\n'.join(map(str, order)))

if __name__ == '__main__':
    main()