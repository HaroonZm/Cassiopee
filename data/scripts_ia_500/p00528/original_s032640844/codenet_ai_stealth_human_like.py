#!/usr/bin/env python
import sys
import heapq
from collections import defaultdict, deque

class Grid:
    """
    This class helps to search points on a 2D grid by their rows or columns.
    """
    def __init__(self, points):
        self.points_by_axis = {0: defaultdict(list), 1: defaultdict(list)}
        for x, y in points:
            self.points_by_axis[0][x].append((x, y))
            self.points_by_axis[1][y].append((x, y))

    def get_points_on_line(self, axis, line_num):
        return self.points_by_axis[axis][line_num]

    def remove_point(self, point):
        self.points_by_axis[0][point[0]].remove(point)
        self.points_by_axis[1][point[1]].remove(point)

    def get_lines(self, axis):
        return self.points_by_axis[axis].keys()

class ModernMansion(Grid):
    def __init__(self, switches, goal):
        super().__init__(switches)
        self.goal = goal

    def remove_orphans(self):
        """
        Recursively remove switches (points) that are alone on their line,
        except for the start line where x == 1 or if the switch is the goal.
        It's a bit like pruning dead ends.
        """
        queue = deque()
        for axis in (0,1):
            for line in list(self.get_lines(axis)):
                queue.append((axis, line))

        while queue:
            axis, line = queue.pop()
            switches = self.get_points_on_line(axis, line)
            if len(switches) != 1:
                # more than one switch on this line, so keep it
                continue
            sw = switches[0]
            # Keep switches on the start line (x == 1) or the goal, never remove those
            if sw[0] == 1 or sw == self.goal:
                continue

            self.remove_point(sw)
            # Add the next axis line that this point lies on
            next_axis = (axis + 1) % 2
            queue.append((next_axis, sw[next_axis]))

    def has_route(self):
        """
        Checks if there is at least one switch on the goal's row or column line.
        If there are no switches on either line other than goal itself, then route is impossible.
        """
        return len(self.points_by_axis[0][self.goal[0]]) > 1 or len(self.points_by_axis[1][self.goal[1]]) > 1

    def get_switches_on_same_line(self, axis, switch):
        # Generator for switches on same axis line, excluding the current switch
        return (s for s in self.get_points_on_line(axis, switch[axis]) if s != switch)

class Searcher:
    def __init__(self, grid):
        self.grid = grid
        self.queue = []
        self.best_time_to_switch = {}
        # deadlines record lines where no better path exists anymore
        self.deadline = {0: set(), 1: set()}

    def next_depth(self, time, current_switch, axis):
        # If we've reached goal, return the time minus the last switch push time
        if current_switch == self.grid.goal:
            return time - 1

        # If this line has been exhausted (no better path), prune search
        if current_switch[axis] in self.deadline[axis]:
            return

        next_axis = (axis + 1) % 2

        found_better = False
        for sw in self.grid.get_switches_on_same_line(axis, current_switch):
            # Time to reach this switch: current time + distance + 1 (pressing switch)
            next_time = time + abs(sw[next_axis] - current_switch[next_axis]) + 1
            best_time = self.best_time_to_switch.get(sw, float('inf'))
            if best_time <= next_time:
                # If we already have a better or equal time, skip
                continue
            # update best time and add to heap for further exploration
            self.best_time_to_switch[sw] = next_time
            heapq.heappush(self.queue, (next_time, sw, next_axis))
            found_better = True

        if not found_better:
            # no better switch found on this line -> mark line as dead-end
            self.deadline[axis].add(current_switch[axis])

    def search(self):
        """
        Generator that yields times when the goal is reached.
        We start at (1, 0) with direction axis == 0 and time == 0,
        simulating movement rules.
        """
        self.queue.append((0, (1, 0), 0))
        while self.queue:
            result = self.next_depth(*heapq.heappop(self.queue))
            if result is not None:
                # Subtract one to account for first move adjustment (as per original logic)
                yield result - 1

    def search_best(self):
        """
        Just get the best time or -1 if no path found.
        """
        try:
            return next(self.search())
        except StopIteration:
            return -1

if __name__ == "__main__":
    M, N, K = map(int, input().split())
    switches = [tuple(map(int, input().split())) for _ in range(K)]
    switches.append((M, N))  # goal position always included

    mansion = ModernMansion(switches, (M, N))
    mansion.remove_orphans()

    if not mansion.has_route():
        print(-1)
        sys.exit()

    searcher = Searcher(mansion)
    answer = searcher.search_best()
    print(answer)