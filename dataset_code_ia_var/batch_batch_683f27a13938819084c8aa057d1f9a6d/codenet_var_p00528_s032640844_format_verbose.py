import sys
import heapq
from collections import defaultdict, deque

class TwoDimensionalGrid:
    """
    Represents a searchable two-dimensional grid,
    providing efficient row/column lookup for points.
    """
    def __init__(self, grid_points):
        self.axis_point_mapping = {
            0: defaultdict(list),  # Maps x to (x, y) points
            1: defaultdict(list)   # Maps y to (x, y) points
        }
        for x_coordinate, y_coordinate in grid_points:
            self.axis_point_mapping[0][x_coordinate].append((x_coordinate, y_coordinate))
            self.axis_point_mapping[1][y_coordinate].append((x_coordinate, y_coordinate))

    def get_points_along_axis(self, axis_index, axis_value):
        return self.axis_point_mapping[axis_index][axis_value]

    def remove_point(self, point):
        x, y = point
        self.axis_point_mapping[0][x].remove(point)
        self.axis_point_mapping[1][y].remove(point)

    def get_axis_lines(self, axis_index):
        return self.axis_point_mapping[axis_index].keys()

class MansionWithSwitches(TwoDimensionalGrid):
    def __init__(self, switch_points, goal_point):
        super().__init__(switch_points)
        self.goal_point = goal_point

    def remove_isolated_switches(self):
        """
        Recursively removes switches that are the only one in their row or column,
        except for the starting and goal positions.
        """
        processing_queue = deque()
        for axis_index in (0, 1):
            for line_value in self.get_axis_lines(axis_index):
                processing_queue.append((axis_index, line_value))

        while processing_queue:
            axis_index, line_value = processing_queue.pop()
            points_on_line = self.get_points_along_axis(axis_index, line_value)
            if len(points_on_line) != 1:
                continue
            candidate_switch = points_on_line[0]
            if candidate_switch[0] == 1 or candidate_switch == self.goal_point:
                continue
            self.remove_point(candidate_switch)
            next_axis_index = (axis_index + 1) % 2
            processing_queue.append((next_axis_index, candidate_switch[next_axis_index]))

    def is_goal_reachable(self):
        """
        Checks if the goal row/column contains more than just the goal,
        otherwise it's unreachable.
        """
        x_goal, y_goal = self.goal_point
        return (
            len(self.axis_point_mapping[0][x_goal]) > 1 or
            len(self.axis_point_mapping[1][y_goal]) > 1
        )

    def get_other_switches_on_same_line(self, axis_index, current_switch):
        """
        Yields all other switches on the same row or column except the current switch.
        """
        for candidate_switch in self.get_points_along_axis(axis_index, current_switch[axis_index]):
            if candidate_switch != current_switch:
                yield candidate_switch

class ShortestPathSwitchSearcher:
    def __init__(self, mansion_grid):
        self.mansion_grid = mansion_grid
        self.search_queue = []
        self.best_time_to_switch = {}
        self.explored_axis_lines = {0: set(), 1: set()}

    def search_from_switch(self, current_time, current_switch, movement_axis):
        """
        Explores reachable switches via the current axis and accumulates minimal times.
        Returns final time upon reaching the goal.
        """
        if current_switch == self.mansion_grid.goal_point:
            return current_time - 1  # Remove last switch activation time

        if current_switch[movement_axis] in self.explored_axis_lines[movement_axis]:
            return

        alternate_axis = (movement_axis + 1) % 2
        found_next_switch = False

        for next_switch in self.mansion_grid.get_other_switches_on_same_line(movement_axis, current_switch):
            x1, y1 = current_switch
            x2, y2 = next_switch
            step_distance = abs(next_switch[alternate_axis] - current_switch[alternate_axis])
            candidate_time = current_time + step_distance + 1  # Switch activation takes 1 unit time
            recorded_best_time = self.best_time_to_switch.get(next_switch, float('inf'))
            if recorded_best_time <= candidate_time:
                continue
            self.best_time_to_switch[next_switch] = candidate_time
            heapq.heappush(self.search_queue, (candidate_time, next_switch, alternate_axis))
            found_next_switch = True

        if not found_next_switch:
            self.explored_axis_lines[movement_axis].add(current_switch[movement_axis])

    def all_possible_times(self):
        """
        Generator yielding all possible total times to reach the goal,
        minus the first forced move adjustment.
        """
        self.search_queue.append((0, (1, 0), 0))
        while self.search_queue:
            search_result = self.search_from_switch(*heapq.heappop(self.search_queue))
            if search_result:
                yield search_result - 1  # Remove forced initial move (1, 0) to (1, 1)

    def find_shortest_time(self):
        """
        Returns the minimum possible time to reach the goal,
        or -1 if unreachable.
        """
        try:
            return next(self.all_possible_times())
        except StopIteration:
            return -1

if __name__ == '__main__':
    rows_count, columns_count, switches_count = map(int, input().split())
    all_switch_positions = [tuple(map(int, input().split())) for _ in range(switches_count)]
    goal_position = (rows_count, columns_count)
    all_switch_positions.append(goal_position)

    grid_with_switches = MansionWithSwitches(all_switch_positions, goal_position)
    grid_with_switches.remove_isolated_switches()

    if not grid_with_switches.is_goal_reachable():
        print('-1')
        sys.exit()

    mansion_searcher = ShortestPathSwitchSearcher(grid_with_switches)
    shortest_path_result = mansion_searcher.find_shortest_time()
    print(shortest_path_result)