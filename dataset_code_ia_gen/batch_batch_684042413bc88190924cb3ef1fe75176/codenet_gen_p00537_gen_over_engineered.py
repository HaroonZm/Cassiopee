class RailSegment:
    def __init__(self, index: int, paper_fare: int, ic_fare: int, ic_card_cost: int):
        self.index = index
        self.paper_fare = paper_fare
        self.ic_fare = ic_fare
        self.ic_card_cost = ic_card_cost
        self.trip_count = 0

    def compute_paper_cost(self) -> int:
        return self.paper_fare * self.trip_count

    def compute_ic_cost(self) -> int:
        return self.ic_card_cost + self.ic_fare * self.trip_count

    def cost_difference_if_ic(self) -> int:
        """Difference between paper cost and IC cost for this rail segment."""
        return self.compute_paper_cost() - self.compute_ic_cost()

    def should_buy_ic_card(self) -> bool:
        return self.cost_difference_if_ic() > 0


class TripPlan:
    def __init__(self, rail_segments: list, travel_route: list):
        self.rail_segments = rail_segments
        self.travel_route = travel_route  # List of city indices starting from 1
        # Tracks the total cost after optimization
        self.total_cost = 0

    def count_rail_usage(self):
        # Rail segment i connects city i and city i+1
        for day in range(len(self.travel_route) - 1):
            start = self.travel_route[day]
            end = self.travel_route[day + 1]
            if start < end:
                # Travel eastward on rails start..end-1
                for rail_index in range(start, end):
                    self.rail_segments[rail_index - 1].trip_count += 1
            else:
                # Travel westward on rails end..start-1
                for rail_index in range(end, start):
                    self.rail_segments[rail_index - 1].trip_count += 1

    def calculate_minimum_cost(self):
        self.count_rail_usage()
        # Initially, assume all trips are by paper tickets
        total_cost = sum(segment.compute_paper_cost() for segment in self.rail_segments)

        # Consider buying IC card for each rail segment if beneficial
        for segment in self.rail_segments:
            if segment.trip_count == 0:
                continue  # No travel on this rail, skip
            if segment.should_buy_ic_card():
                # Change cost from paper to IC for this segment
                cost_with_ic = segment.compute_ic_cost()
                cost_with_paper = segment.compute_paper_cost()
                total_cost += cost_with_ic - cost_with_paper

        self.total_cost = total_cost
        return total_cost


class InputReader:
    @staticmethod
    def read_ints():
        return list(map(int, input().split()))

    @classmethod
    def read_problem_instance(cls):
        N, M = cls.read_ints()
        travel_route = cls.read_ints()
        rail_segments = []
        for i in range(1, N):
            A_i, B_i, C_i = cls.read_ints()
            rail_segments.append(RailSegment(i, A_i, B_i, C_i))
        return N, M, travel_route, rail_segments


class Solver:
    def __init__(self):
        self.N = None
        self.M = None
        self.travel_route = None
        self.rail_segments = None
        self.trip_plan = None

    def load_data(self):
        self.N, self.M, self.travel_route, self.rail_segments = InputReader.read_problem_instance()
        self.trip_plan = TripPlan(self.rail_segments, self.travel_route)

    def solve(self):
        return self.trip_plan.calculate_minimum_cost()


def main():
    solver = Solver()
    solver.load_data()
    result = solver.solve()
    print(result)


if __name__ == '__main__':
    main()