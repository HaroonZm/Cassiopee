from typing import List, Tuple, Union, Iterable
import sys
import bisect

sys.setrecursionlimit(10**7)

# Constants
MAX_DAY = 3_652_425
MANY_YEARS_LATER_MSG = "Many years later"

# Abstract base class for different recovery increment functions
class RecoveryIncrementStrategy:
    def daily_increment_sum(self, days: int) -> int:
        raise NotImplementedError

    def prefix_sum(self, days: int) -> int:
        raise NotImplementedError

# Concrete strategies for type 0, 1, 2
class IncrementType0(RecoveryIncrementStrategy):
    # Each day adds +1 independently of d
    def daily_increment_sum(self, days: int) -> int:
        return days

    def prefix_sum(self, days: int) -> int:
        # Sum of 1 for each day
        return days

class IncrementType1(RecoveryIncrementStrategy):
    # Each day adds d (day index counting from 1)
    # sum_{d=1}^x d = x*(x+1)//2
    def daily_increment_sum(self, days: int) -> int:
        return days * (days + 1) // 2

    def prefix_sum(self, days: int) -> int:
        # Sum of sums = sum_{k=1}^days (k*(k+1)/2)
        # = (days*(days+1)*(days+2)) // 6
        return days * (days + 1) * (days + 2) // 6

class IncrementType2(RecoveryIncrementStrategy):
    # Each day adds d^2 (day index counting from 1)
    # sum_{d=1}^x d^2 = x(x+1)(2x+1)/6
    def daily_increment_sum(self, days: int) -> int:
        return days * (days + 1) * (2 * days + 1) // 6

    def prefix_sum(self, days: int) -> int:
        # sum_{k=1}^days sum_{d=1}^k d^2
        # = sum_{k=1}^days [k(k+1)(2k+1)/6]
        # There is a closed form:
        # sum_{k=1}^n k^3 + 3*k^2 + 2*k all / 6
        # Actually let's precompute because days<=10^4
        # But to keep sophisticated, implement formula with Faulhaber's formula:
        # sum k(k+1)(2k+1) = 2*sum k^3 + 3*sum k^2 + sum k
        # sum k = n(n+1)/2
        # sum k^2 = n(n+1)(2n+1)/6
        # sum k^3 = (n(n+1)/2)^2
        n = days
        sum_k = n * (n + 1) // 2
        sum_k2 = n * (n + 1) * (2 * n + 1) // 6
        sum_k3 = sum_k * sum_k
        return (2 * sum_k3 + 3 * sum_k2 + sum_k) // 6

# Factory for strategy
def strategy_factory(t: int) -> RecoveryIncrementStrategy:
    if t == 0:
        return IncrementType0()
    elif t == 1:
        return IncrementType1()
    else:
        return IncrementType2()

# Data class for Service
class Service:
    def __init__(self, w: int, t: int, x: int, idx: int):
        self.w = w
        self.t = t
        self.x = x
        self.idx = idx
        self.recovery_day: Union[int, None] = None

# Abstract class to represent a recovery interval effect
class RecoveryEffect:
    def __init__(self, start_day: int, strategy: RecoveryIncrementStrategy, duration: int):
        self.start_day = start_day
        self.strategy = strategy
        self.duration = duration

    def effect_on_day(self, day: int) -> int:
        d = day - self.start_day + 1
        if d < 1 or d > self.duration:
            return 0
        if isinstance(self.strategy, IncrementType0):
            return 1
        elif isinstance(self.strategy, IncrementType1):
            return d
        else:
            return d * d

    def total_effect_up_to_day(self, day: int) -> int:
        # total effect accumulated from start_day to day
        if day < self.start_day:
            return 0
        days_active = min(day - self.start_day + 1, self.duration)
        if days_active <= 0:
            return 0
        return self.strategy.daily_increment_sum(days_active)

# Class managing all increments and queries for recovery progress
class RecoveryAccumulator:
    def __init__(self, base_increment: int = 1):
        self.base_increment = base_increment
        self.services: List[Service] = []
        self.effects: List[RecoveryEffect] = []
        self.recovery_days: List[int] = []
        self.recovery_map: dict = dict()

    def add_service(self, service: Service) -> None:
        self.services.append(service)

    def prepare(self) -> None:
        # Sort services by w already guaranteed according to problem
        self.services.sort(key=lambda s: s.w)
        self.recovery_days = [None] * len(self.services)

    def compute_recovery_days(self) -> None:
        # We'll find recovery days for services in ascending w order
        # We'll simulate recovery day calculation via binary search per service

        # To keep sophistication, perform event-driven approach with incremental day search
        # but binary search approach for large constraints

        # We will precompute total increments per day efficiently using prefix sums
        # But as complexity would be too high, we do simulation with binary search

        max_w = self.services[-1].w if self.services else 0

        # Binary search search upper bound estimation
        ub = max_w + 10**8  # big upper bound to be sure

        # For efficiency and abstraction: create a sub-class to compute cumulative recovery degree
        class RecoveryDegreeQuery:
            def __init__(self, services: List[Service]):
                self.services = services

            def degree_on(self, day: int) -> int:
                # Base increment day
                total = day
                for svc in self.services:
                    if svc.recovery_day is not None:
                        sday = svc.recovery_day + 1
                        eday = svc.recovery_day + svc.x
                        if sday <= day <= eday:
                            d = day - svc.recovery_day
                            if svc.t == 0:
                                total += 1
                            elif svc.t == 1:
                                total += d
                            else:
                                total += d * d
                        elif day > eday:
                            # sum full duration increments
                            if svc.t == 0:
                                total += svc.x
                            elif svc.t == 1:
                                total += svc.x * (svc.x + 1) // 2
                            else:
                                total += svc.x * (svc.x + 1) * (2 * svc.x + 1) // 6
                return total

        rq = RecoveryDegreeQuery(self.services)

        for svc in self.services:
            if svc.w == 0:
                svc.recovery_day = 0
                continue
            # Binary search day d where recovery degree >= w_i
            left, right = 0, ub
            while left < right:
                mid = (left + right) // 2
                val = rq.degree_on(mid)
                if val >= svc.w:
                    right = mid
                else:
                    left = mid + 1
            svc.recovery_day = left

            # Fix for many years later cutoff
            if svc.recovery_day > MAX_DAY:
                svc.recovery_day = None

        self.services.sort(key=lambda s: s.idx)

    def output_recovery_days(self) -> Iterable[str]:
        for svc in self.services:
            if svc.recovery_day is None:
                yield MANY_YEARS_LATER_MSG
            else:
                yield str(svc.recovery_day)

    def compute_recovery_degree(self, queries: List[int]) -> List[int]:
        # Instead of simulating day by day, for sophistication, we decompose

        # We'll generate a timeline of all recovery day intervals and their influence type.
        # Use difference arrays and prefix computations.

        # Collect all intervals of effects: (start_day, +effect), (end_day+1, -effect)
        # But as effect is complex (non-linear per day), we precompute partial sums of increments per service.

        # Create events for each service's effect start and end+1
        # For each query, calculate base + sum of active increments

        # We'll manage three Fenwick trees or BITs (or segmented sums) for types 0, 1, 2 since increments differ
        # But since durations x_i <= 10^4 and N <= 10^5, with Q <= 10^5 and queries up to MAX_DAY,
        # use line sweep with all event points to handle queries efficiently

        # Gather all event days: recovery_day+1 (effect start), recovery_day+x_i+1 (effect end+1)
        events = []
        type0 = []
        type1 = []
        type2 = []
        for svc in self.services:
            if svc.recovery_day is not None:
                start = svc.recovery_day + 1
                end = start + svc.x - 1
                # For effect range queries, we'll mark start and end+1 (for removal)
                events.append((start, 1, svc.t))
                events.append((end + 1, -1, svc.t))
        # Add all queries as events for processing
        for i, q in enumerate(queries):
            events.append((q, 0, i))  # 0 marker for query event

        # Sort all events by day ascending, queries after effect events if same day
        # So effects (+1/-1) plan to be processed before queries on same day
        events.sort(key=lambda x: (x[0], x[1]))

        # Counters of how many active effects per type
        active_effects = [0, 0, 0]

        # We'll track sums of increments contributed by active effects until current day
        # To compute increments at day y_j, we need for each active effect type:
        # sum of increments for range since effect started to day y_j

        # To keep track of effect start days for each active effect type,
        # we maintain a list of (recovery_day+1) for each activated effect

        # But multiple services with same type can overlap; since for max x_i=10^4, and max active effects is
        # bounded by N=10^5, this might be too large to iterate on each query.

        # Approach: since each effect contributes increments depending on d relative to start day,
        # sum increments over active effects = sum_over_effects of f(d)
        # If multiple effects active of same type, sum their start days and count.

        # Maintain for each type a sorted list of start days of active effects;

        # For sophistication: precompute prefix sums of increments for days 0..max query day + x_i max to accelerate queries

        # But memory too large, so another approach:

        # Because x_i ≤ 10^4, queries ≤ 10^5, let's store effect intervals in a structure allowing cumulative increments

        # Final approach: for each service effect interval, add their increments on days start to start+x_i-1 to a dict keyed by day.

        # For each day in queries, recover total increments = base day + sum effects increments

        # Since MAX_DAY is 3,652,425, and we only have Q <= 10^5 queries, we will only compute increments at query days.

        # For each service effect, precompute increments at days relevant to queries via binary search

        # We'll gather all query days and service effect days.

        # Final design: For each query day y_j,
        #   - base = y_j
        #   - for each service: if y_j in [recovery_day+1, recovery_day+x_i], add increments from that day's d

        # To avoid O(NQ), we map queries and services in sorted order, then for each service:
        #   find the range of queries affected and precompute increments sum from d.

        # Implement post-processing query approach:

        q_results = [0] * len(queries)
        # Sort queries with indexes
        queries_with_idx = sorted((day, i) for i, day in enumerate(queries))

        # For each service with recovery_day defined, process queries in effect range and add increments
        # To accelerate lookups, we'll use binary search on queries_with_idx to find affected queries

        q_days = [qd for qd, _ in queries_with_idx]

        # Initialize results with base increments (just the day itself)
        for day, idx in queries_with_idx:
            q_results[idx] = day

        for svc in self.services:
            if svc.recovery_day is None:
                continue
            s_start = svc.recovery_day + 1
            s_end = s_start + svc.x -1
            if s_end < queries_with_idx[0][0]:
                continue  # no query in effect range
            # Find queries inside effect interval
            left_i = bisect.bisect_left(q_days, s_start)
            right_i = bisect.bisect_right(q_days, s_end)

            strat = strategy_factory(svc.t)

            for qi in range(left_i, right_i):
                day = q_days[qi]
                d = day - svc.recovery_day
                increment = 1
                if svc.t == 0:
                    increment = 1
                elif svc.t == 1:
                    increment = d
                else:
                    increment = d * d
                idx = queries_with_idx[qi][1]
                q_results[idx] += increment

        return q_results

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    services = [None] * N
    for i in range(N):
        w, t, x = map(int, input().split())
        services[i] = Service(w, t, x, i)
    queries = [int(input()) for _ in range(Q)]

    accumulator = RecoveryAccumulator()
    for svc in services:
        accumulator.add_service(svc)
    accumulator.prepare()
    accumulator.compute_recovery_days()

    for line in accumulator.output_recovery_days():
        print(line)

    results = accumulator.compute_recovery_degree(queries)
    for val in results:
        print(val)

if __name__ == "__main__":
    main()