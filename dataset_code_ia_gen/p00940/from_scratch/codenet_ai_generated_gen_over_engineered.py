from typing import List, Tuple, Dict, Set
import sys

class Process:
    def __init__(self, pid: int, resource_needs: List[int]):
        self.pid: int = pid
        self.resource_needs: List[int] = resource_needs[:]  # total needs per resource kind
        self.held_resources: List[int] = [0]*len(resource_needs)  # currently held instances per resource kind
        self.finished: bool = False

    def need(self) -> List[int]:
        return [need - held for need, held in zip(self.resource_needs, self.held_resources)]

    def is_finished(self) -> bool:
        return self.finished or all((need == 0 for need in self.need()))

    def try_finish(self) -> bool:
        # Mark as finished and release resources if finished.
        if self.is_finished() and not self.finished:
            self.finished = True
            return True
        return False

class ResourceManager:
    def __init__(self, p_count: int, r_count: int, initial_available: List[int], processes_needs: List[List[int]]):
        self.p_count: int = p_count
        self.r_count: int = r_count
        self.available: List[int] = initial_available[:]  # available instances of each resource

        self.processes: List[Process] = [Process(pid=i+1, resource_needs=processes_needs[i]) for i in range(p_count)]

    def allocate(self, pid: int, rid: int) -> None:
        # Allocate one instance of rid resource to process pid.
        proc: Process = self.processes[pid-1]
        self.available[rid-1] -= 1
        proc.held_resources[rid-1] += 1

    def release_all(self, pid: int) -> None:
        proc = self.processes[pid-1]
        for i in range(self.r_count):
            self.available[i] += proc.held_resources[i]
            proc.held_resources[i] = 0

    def can_finish_with_available(self, proc: Process, work: List[int]) -> bool:
        # Check if proc's remaining need can be satisfied with work vector
        return all((need <= w for need, w in zip(proc.need(), work)))

    def is_deadlock_avoidable(self) -> bool:
        '''
        Implements a Banker's algorithm style safety check:
        - work: simulated available resource vector
        - finish: processed array of booleans for processes finished in simulation
        '''
        work = self.available[:]
        finish = [proc.finished for proc in self.processes]

        progress = True
        while progress:
            progress = False
            for i, proc in enumerate(self.processes):
                if finish[i]:
                    continue
                if self.can_finish_with_available(proc, work):
                    # simulate finishing proc: release held resources
                    for rid in range(self.r_count):
                        work[rid] += proc.held_resources[rid]
                    finish[i] = True
                    progress = True  # found a process that can finish, so continue searching
        # If all finish are True, no deadlock unavoidable state
        return all(finish)

class DeadlockDetectionSolution:
    def __init__(self):
        self.p: int = 0  # number of processes
        self.r: int = 0  # number of resources
        self.t: int = 0  # length of time log
        self.l: List[int] = []  # initial available resources
        self.n: List[List[int]] = []  # process needs
        self.logs: List[Tuple[int,int]] = []  # log entries (process, resource)

    def input_data(self):
        input_line = sys.stdin.readline()
        while input_line.strip() == '':
            input_line = sys.stdin.readline()
        self.p, self.r, self.t = map(int, input_line.strip().split())
        self.l = list(map(int, sys.stdin.readline().strip().split()))
        self.n = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(self.p)]
        self.logs = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(self.t)]

    def solve(self) -> int:
        manager = ResourceManager(self.p, self.r, self.l, self.n)

        for time_idx, (pid, rid) in enumerate(self.logs, start=1):
            manager.allocate(pid, rid)

            # After allocation, we try to finish any process that can finish now
            # keeps releasing resources of finished processes until no new process finishes
            finished_this_round = True
            while finished_this_round:
                finished_this_round = False
                for proc in manager.processes:
                    if proc.try_finish():
                        # release resources
                        manager.release_all(proc.pid)
                        finished_this_round = True

            # check if deadlock unavoidable
            if not manager.is_deadlock_avoidable():
                return time_idx

        # if never found deadlock unavoidable
        return -1

def main():
    solution = DeadlockDetectionSolution()
    solution.input_data()
    print(solution.solve())

if __name__ == "__main__":
    main()