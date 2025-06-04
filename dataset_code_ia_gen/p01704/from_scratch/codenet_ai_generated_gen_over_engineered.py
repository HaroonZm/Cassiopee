import sys
import math
from typing import List, Tuple, Optional, Iterator

class VitalityConstraint:
    """
    Represents the vitality constraint for a single flower plant.
    Ensures that: W * vw_i + F_i * vf_i >= th_i, with W,F_i >= 0.
    """

    __slots__ = ('vw', 'pf', 'vf', 'th')

    def __init__(self, vw: float, pf: float, vf: float, th: float):
        self.vw = vw  # Water effect coefficient on vitality for plant i
        self.pf = pf  # Fertilizer cost per kg for plant i
        self.vf = vf  # Fertilizer vitality effect for plant i (positive)
        self.th = th  # Vitality threshold for plant i

    def min_fertilizer_for_water(self, W: float) -> float:
        """
        Given water amount W, compute minimal fertilizer F_i needed to
        satisfy vitality constraint.
        F_i = max(0, (th_i - W * vw_i) / vf_i)
        """
        needed = (self.th - W * self.vw) / self.vf
        return max(0.0, needed)

    def cost_for_fertilizer(self, F: float) -> float:
        """
        Compute fertilizer cost for given F_i.
        """
        return F * self.pf


class FlowerPlantSystem:
    """
    Abstracts the entire system of plants, watering, fertilizers,
    and computing minimal cost to achieve flowering simultaneously.
    """

    __slots__ = ('num_plants', 'pw', 'constraints')

    def __init__(self, num_plants: int, pw: float, constraints: List[VitalityConstraint]):
        self.num_plants = num_plants
        self.pw = pw  # Cost per liter of water
        self.constraints = constraints

    def _cost_function(self, W: float) -> float:
        """
        Given an amount of water W, compute the total cost:
        cost = W * pw + sum_i F_i * pf_i
        where F_i = max(0, (th_i - W*vw_i)/vf_i)
        """
        total_cost = W * self.pw
        for con in self.constraints:
            F_i = con.min_fertilizer_for_water(W)
            total_cost += con.cost_for_fertilizer(F_i)
        return total_cost

    def _is_feasible(self, W: float) -> bool:
        """
        Check if watering W liters can satisfy all constraints
        with some non-negative fertilizer F_i.
        It is always feasible if F_i >= 0 can satisfy equations,
        but problem constraints assert this.
        """
        # Since F_i can be unbounded upwards, always feasible.
        return W >= 0

    def solve(self) -> float:
        """
        Solve for minimal cost using ternary search on W in [0, W_max].
        W_max is chosen large enough so all th_i <= W * vw_i 
        (i.e. no fertilizer needed), or we can pick a sufficiently high upper bound.
        """

        # Find W_max so that for all i: W_max * vw_i >= th_i (if vw_i > 0)
        W_max_candidates = []
        for con in self.constraints:
            if con.vw > 0:
                # W >= th_i / vw_i
                W_max_candidates.append(max(0.0, con.th / con.vw))
            elif con.vw < 0:
                # Watering hurts this plant vitality.
                # Probably high watering is bad, so no upper bound from here.
                pass
            else:
                # vw_i == 0, fertilizer must cover threshold anyway.
                pass
        W_max_candidates.append(0)
        initial_max = max(W_max_candidates) * 2 + 100.0  # Add margin for exploration

        # If all vw_i <= 0, watering may be useless, so limit W_max
        import math
        if initial_max < 1.0:
            initial_max = 100.0  # Arbitrary upper bound

        left = 0.0
        right = initial_max

        # Ternary search for minimum cost on continuous domain [left,right]
        for _ in range(100):
            m1 = left + (right - left) / 3
            m2 = right - (right - left) / 3
            c1 = self._cost_function(m1)
            c2 = self._cost_function(m2)
            if c1 > c2:
                left = m1
            else:
                right = m2

        optimal_W = (left + right) / 2
        minimal_cost = self._cost_function(optimal_W)
        # Since costs can be fractional, format with required precision by caller
        return minimal_cost


class InputParser:
    """
    Sophisticated parser to handle large input and multiple datasets,
    abstracting raw sys.stdin input iterations.
    """

    __slots__ = ('lines',)

    def __init__(self, input_stream: Iterator[str]):
        self.lines = input_stream

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[int, int, List[VitalityConstraint]]:
        # Read one dataset: N
        while True:
            line = next(self.lines).strip()
            if not line:
                continue
            N = int(line)
            if N == 0:
                raise StopIteration
            break

        # Read pw
        while True:
            line = next(self.lines).strip()
            if line:
                pw = int(line)
                break

        constraints = []
        read_lines = 0
        while read_lines < N:
            line = next(self.lines).strip()
            if not line:
                continue
            vw_i, pf_i, vf_i, th_i = map(int, line.split())
            c = VitalityConstraint(vw=float(vw_i), pf=float(pf_i),
                                   vf=float(vf_i), th=float(th_i))
            constraints.append(c)
            read_lines += 1

        return (N, pw, constraints)


def main():
    input_stream = (line for line in sys.stdin)
    parser = InputParser(input_stream)

    output = []
    for dataset in parser:
        N, pw, constraints = dataset
        system = FlowerPlantSystem(N, float(pw), constraints)
        result = system.solve()
        output.append(f"{result:.10f}")

    # Print results, stripping unnecessary zeros
    for line in output:
        # Python float formatting to match problem error constraints:
        # relative or absolute error within 1e-4 allowed
        # So 6 decimal places is enough. Adjust accordingly.
        f = float(line)
        print(f"{f:.6f}".rstrip('0').rstrip('.') if '.' in f"{f:.6f}" else f"{f:.6f}")

if __name__ == "__main__":
    main()