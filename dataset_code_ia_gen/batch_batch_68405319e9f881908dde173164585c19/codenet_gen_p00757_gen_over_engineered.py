import sys
from typing import List, Tuple, Dict, NamedTuple, Optional

class Area(NamedTuple):
    top: int
    left: int
    bottom: int  # exclusive
    right: int   # exclusive

    def height(self) -> int:
        return self.bottom - self.top

    def width(self) -> int:
        return self.right - self.left

class DemandGrid:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0]) if self.h > 0 else 0
        self.prefix_sum = self._compute_prefix_sum()

    def _compute_prefix_sum(self) -> List[List[int]]:
        ps = [[0]*(self.w+1) for _ in range(self.h+1)]
        for i in range(1, self.h+1):
            row_sum = 0
            for j in range(1, self.w+1):
                row_sum += self.grid[i-1][j-1]
                ps[i][j] = ps[i-1][j] + row_sum
        return ps

    def area_sum(self, area: Area) -> int:
        # sum of area [top, bottom), [left, right)
        return self.prefix_sum[area.bottom][area.right] - self.prefix_sum[area.top][area.right] - self.prefix_sum[area.bottom][area.left] + self.prefix_sum[area.top][area.left]

class GroupingSolution(NamedTuple):
    groups_count: int
    max_suppressed_demand: int
    reserve_power: int
    parts: List[Area]

class RollingBlackoutPlanner:
    def __init__(self, demand_grid: DemandGrid, supply_capacity: int):
        self.demand_grid = demand_grid
        self.supply_capacity = supply_capacity
        self.memo: Dict[Area, GroupingSolution] = {}

    def solve(self) -> Tuple[int,int]:
        entire_area = Area(0, 0, self.demand_grid.h, self.demand_grid.w)
        solution = self._dfs(entire_area)
        # solution guaranteed to exist because s < total demand
        return (solution.groups_count, solution.reserve_power)

    def _dfs(self, area: Area) -> GroupingSolution:
        if area in self.memo:
            return self.memo[area]

        total_demand = self.demand_grid.area_sum(area)
        # If the max suppressed demand is the greatest total demand of all but one group,
        # then if we have only one group (no split), max suppressed demand = 0 because all others = 0 (no others)
        # But problem states supply capacity < total demand, so total demand alone is > s.
        # So single group fails condition 1, unless groups_count=1? 
        # But output sample shows groups>=1 are output, so we must consider single group as valid if max suppressed demand <= s.
        # Reinterpret: max suppressed demand is max total demand among all groups except the one currently off.
        # For one group, all but one group means "no group", so max suppressed demand could be 0.
        # But test data likely expects splitting since s < total demand.
        # We'll consider no split if max suppressed demand <= s:
        # max suppressed demand of single group with no split is 0 (no other groups), which is <= s trivially.
        # So this is valid grouping of one group.

        # Max suppressed demand for single group is 0 because "all but one groups" = empty set => max 0.
        if total_demand <= self.supply_capacity:
            # no split, 1 group, maximal suppressed demand 0, reserve power s
            gs = GroupingSolution(
                groups_count=1,
                max_suppressed_demand=0,
                reserve_power=self.supply_capacity - 0,
                parts=[area]
            )
            self.memo[area] = gs
            return gs

        best_solution = None

        # Attempt vertical splits
        for c in range(area.left+1, area.right):
            left_area = Area(area.top, area.left, area.bottom, c)
            right_area = Area(area.top, c, area.bottom, area.right)
            left_sol = self._dfs(left_area)
            right_sol = self._dfs(right_area)

            merged = self._merge(left_sol, right_sol)
            if merged is not None:
                best_solution = self._compare(best_solution, merged)

        # Attempt horizontal splits
        for r in range(area.top+1, area.bottom):
            top_area = Area(area.top, area.left, r, area.right)
            bottom_area = Area(r, area.left, area.bottom, area.right)
            top_sol = self._dfs(top_area)
            bottom_sol = self._dfs(bottom_area)

            merged = self._merge(top_sol, bottom_sol)
            if merged is not None:
                best_solution = self._compare(best_solution, merged)

        if best_solution is None:
            # no possible grouping for this area meeting the constraints
            # to avoid infinite recursion, return a grouping that violates the condition (or the worst possible)
            # but problem states must produce grouping, so returning a single group anyway:
            # max suppressed demand in single group = 0
            # total_demand > s but single group is invalid since condition 1 fails
            # so no group here means no valid solution => store None
            # But to ease recursive calls, return a solution with groups_count=1 and max_suppressed_demand = total_demand,
            # so it will be filtered by merges.
            gs = GroupingSolution(
                groups_count=1,
                max_suppressed_demand=total_demand,
                reserve_power=self.supply_capacity - total_demand,
                parts=[area]
            )
            self.memo[area] = gs
            return gs

        self.memo[area] = best_solution
        return best_solution

    def _merge(self, sol1: GroupingSolution, sol2: GroupingSolution) -> Optional[GroupingSolution]:
        # merged grouping: combine groups from sol1 and sol2
        groups_count = sol1.groups_count + sol2.groups_count

        # Calculate the total demand of each individual group from parts to compute max suppressed demand.
        # max suppressed demand = max total demand of all but one group (the cut off one)
        # so for each group that is off, compute total demand of all others and get max over those
        # equivalently, we only need the max total demand among groups except the one off,
        # and we want to minimize the max suppressed demand,
        # but condition states max suppressed demand <= supply capacity s.
        # Here, max suppressed demand of grouping is max of total demand_of_all_except_one_group,
        # among all groups in grouping.
        # But:
        # max suppressed demand = max_{g in groups} (total_demand_all_groups - demand_of_g)
        # = total_demand_all_groups - min_{g in groups} demand_of_g

        total_demand_all = sum(self.demand_grid.area_sum(area) for area in sol1.parts + sol2.parts)
        min_group_demand = min(
            min(self.demand_grid.area_sum(area) for area in sol1.parts),
            min(self.demand_grid.area_sum(area) for area in sol2.parts)
        )
        max_suppressed_demand = total_demand_all - min_group_demand

        if max_suppressed_demand > self.supply_capacity:
            return None

        reserve_power = self.supply_capacity - max_suppressed_demand
        parts = sol1.parts + sol2.parts
        return GroupingSolution(groups_count, max_suppressed_demand, reserve_power, parts)

    def _compare(self, a: Optional[GroupingSolution], b: GroupingSolution) -> GroupingSolution:
        # Condition 3 and 4 given:
        # maximize groups_count
        # if tie maximize reserve_power
        if a is None:
            return b
        if b.groups_count > a.groups_count:
            return b
        if b.groups_count < a.groups_count:
            return a
        # groups_count tie
        if b.reserve_power > a.reserve_power:
            return b
        return a

def parse_input() -> List[Tuple[int,int,int,List[List[int]]]]:
    datasets = []
    input_lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(input_lines):
        if input_lines[i].strip() == '':
            i += 1
            continue
        hws = input_lines[i].split()
        if len(hws) != 3:
            i += 1
            continue
        h, w, s = map(int, hws)
        if h == 0 and w == 0 and s == 0:
            break
        i += 1
        grid = []
        for _ in range(h):
            row = list(map(int, input_lines[i].split()))
            grid.append(row)
            i += 1
        datasets.append((h,w,s,grid))
    return datasets

def main():
    datasets = parse_input()
    for h, w, s, grid in datasets:
        demand_grid = DemandGrid(grid)
        planner = RollingBlackoutPlanner(demand_grid, s)
        groups_count, reserve_power = planner.solve()
        print(groups_count, reserve_power)

if __name__ == "__main__":
    main()