class TrainingMachine:
    def __init__(self, index: int, tickets: int, calorie: int):
        self.index = index
        self.tickets = tickets
        self.calorie = calorie
        self.used = 0  # How many times machine is used in final solution

class Constraint:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

class MaxCaloriesOptimizer:
    def __init__(self, machines, constraints):
        self.machines = machines
        self.constraints = constraints
        self.N = len(machines)
        self.R = len(constraints)

    def _build_graph(self):
        # Build graph for difference constraints of form x_a - x_b <= c
        graph = {i: [] for i in range(self.N)}
        for c in self.constraints:
            a = c.a - 1
            b = c.b - 1
            cost = c.c
            graph[b].append((a, cost))  # x_a - x_b <= c  => x_a <= x_b + c => x_b -(->) x_a with weight c
        self.graph = graph

    def _bellman_ford(self):
        # Use Bellman-Ford algorithm to find maximal x_i subject to constraints and 0<= x_i <= t_i
        dist = [float('inf')] * self.N
        # Dist interpreted as upper bound offset for usage of machines
        # To maximize calories, we want to assign x_i as large as possible but within tickets and constraints
        # Because constraints are x_a - x_b <= c, rearranged as x_a <= x_b + c,
        # treating x_b as base, x_a is upper bounded by x_b + c.
        dist = [-float('inf')] * self.N  # Store lower bounds for x_i (maximizing usage)
        # We need to find maximal x_i satisfying x_a - x_b <= c thus x_a <= x_b + c
        # Initialize dist with 0 as minimum lower bound is 0
        for i in range(self.N):
            dist[i] = 0

        # Relax edges R times
        for _ in range(self.R):
            updated = False
            for c in self.constraints:
                a = c.a - 1
                b = c.b - 1
                if dist[a] > dist[b] + c.c:
                    dist[a] = dist[b] + c.c
                    updated = True
            if not updated:
                break

        # dist[i] is an upper bound on x_i from constraints
        return dist

    def _adjust_usages(self, dist):
        # Determine maximum feasible usage x_i for each machine
        # x_i <= t_i (tickets)
        # x_i <= dist[i] (constraints upper bound)
        # x_i >= 0
        usage = [0] * self.N
        for i, machine in enumerate(self.machines):
            # Because dist[i] might be +inf or invalid (no feasible solution means -inf?), clamp it
            upper_bound = dist[i]
            if upper_bound == float('inf'):
                upper_bound = machine.tickets
            upper_bound = min(upper_bound, machine.tickets)
            if upper_bound < 0:
                upper_bound = 0
            usage[i] = int(upper_bound)
        return usage

    def _fix_violation(self, usage):
        # The previous step might not guarantee all constraints are met, fix by iterative relaxation
        # Repeatedly enforce x_a - x_b <= c constraints, adjust usage down if violated
        changed = True
        while changed:
            changed = False
            for c in self.constraints:
                a = c.a - 1
                b = c.b - 1
                if usage[a] > usage[b] + c.c:
                    old = usage[a]
                    usage[a] = usage[b] + c.c
                    if usage[a] < 0:
                        usage[a] = 0
                    if usage[a] != old:
                        changed = True
        return usage

    def maximize_calories(self):
        self._build_graph()
        dist = self._bellman_ford()
        usage = self._adjust_usages(dist)
        usage = self._fix_violation(usage)
        total_calories = 0
        for i, u in enumerate(usage):
            total_calories += u * self.machines[i].calorie
        return total_calories

class GymSimulator:
    def __init__(self):
        self.machines = []
        self.constraints = []

    def read_input(self):
        import sys
        input = sys.stdin.readline
        N, R = map(int, input().split())
        self.N = N
        self.R = R
        for i in range(N):
            t, e = map(int, input().split())
            self.machines.append(TrainingMachine(i, t, e))
        for _ in range(R):
            a, b, c = map(int, input().split())
            self.constraints.append(Constraint(a, b, c))

    def solve(self):
        optimizer = MaxCaloriesOptimizer(self.machines, self.constraints)
        ans = optimizer.maximize_calories()
        print(ans)

if __name__ == "__main__":
    simulator = GymSimulator()
    simulator.read_input()
    simulator.solve()