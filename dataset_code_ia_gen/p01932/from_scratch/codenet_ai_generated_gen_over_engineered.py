import sys
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional


class Employee:
    def __init__(self, arrival_time: int, floor: int):
        self.arrival_time = arrival_time
        self.floor = floor
        self.onboard = False
        self.board_time = None  # time the employee actually boarded
        self.exit_time = None   # time the employee reached 1F via elevator


class ElevatorState(ABC):
    @abstractmethod
    def next_action(self):
        pass


class Elevator:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_floor = 1
        self.current_time = 0
        self.passengers: List[Employee] = []
        self.total_onboard_time = 0

    def move_to_floor(self, target_floor: int):
        distance = abs(target_floor - self.current_floor)
        self.current_time += distance
        self.current_floor = target_floor

    def wait_until(self, time: int):
        if time > self.current_time:
            self.current_time = time

    def can_board(self):
        return len(self.passengers) < self.capacity

    def board_employee(self, emp: Employee):
        emp.onboard = True
        emp.board_time = self.current_time
        self.passengers.append(emp)

    def disembark_all(self):
        for emp in self.passengers:
            emp.exit_time = self.current_time
            self.total_onboard_time += emp.exit_time - emp.board_time
        self.passengers.clear()

    def operate(self, employees: List[Employee]) -> int:
        # We will sort employees by floor ascending so we visit floors in order
        # That helps minimize elevator travel and waiting times
        floor_groups = {}
        for emp in employees:
            floor_groups.setdefault(emp.floor, []).append(emp)
        floors_sorted = sorted(floor_groups.keys())

        for floor in floors_sorted:
            emps = floor_groups[floor]
            # Move elevator to floor
            self.move_to_floor(floor)
            # Wait until the earliest arrival time among employees at this floor
            earliest_arrival = emps[0].arrival_time
            self.wait_until(earliest_arrival)
            # Attempt boarding in arrival time order:
            # employees appear ordered by arrival times per problem constraint
            emps = sorted(emps, key=lambda e: e.arrival_time)
            for emp in emps:
                # Employee can only board if elevator is on floor at emp.arrival_time or later
                # and capacity allows
                if self.current_time >= emp.arrival_time and self.can_board():
                    self.board_employee(emp)
                else:
                    # Employee must walk down stairs, cannot be carried
                    return -1

            # After boarding all possible, go down to floor 1 with all passengers
            self.move_to_floor(1)
            self.disembark_all()

        return self.total_onboard_time


class InputParser:
    def __init__(self):
        self.N = 0
        self.D = 0
        self.employees: List[Employee] = []

    def parse(self):
        input = sys.stdin.read().strip().split()
        self.N = int(input[0])
        self.D = int(input[1])
        records = input[2:]
        self.employees = [Employee(int(records[i * 2]), int(records[i * 2 + 1])) for i in range(self.N)]


class Solution:
    def __init__(self):
        self.parser = InputParser()
        self.elevator: Optional[Elevator] = None

    def run(self):
        self.parser.parse()
        employees = self.parser.employees
        # Validate strictly increasing t_i (given by problem constraints)
        for i in range(len(employees) - 1):
            if employees[i].arrival_time >= employees[i + 1].arrival_time:
                print(-1)
                return
        self.elevator = Elevator(self.parser.D)
        cost = self.elevator.operate(employees)
        print(cost)


if __name__ == "__main__":
    solution = Solution()
    solution.run()