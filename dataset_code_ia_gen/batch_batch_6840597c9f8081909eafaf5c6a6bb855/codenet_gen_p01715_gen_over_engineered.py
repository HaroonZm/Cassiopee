class BusStop:
    def __init__(self, index: int, distance: int):
        self.index = index
        self.distance = distance

class Passenger:
    def __init__(self, arrival_time: int, bus_stop: BusStop):
        self.arrival_time = arrival_time
        self.bus_stop = bus_stop

class BusRoute:
    def __init__(self, stops: list):
        self.stops = stops

class BusScheduleOptimizer:
    def __init__(self, route: BusRoute, passengers: list, bus_count: int):
        self.route = route
        self.passengers = passengers
        self.bus_count = bus_count
        self.s = len(route.stops)
        self.n = len(passengers)
        self.m = bus_count

    def _preprocess_passengers(self):
        # Create list of adjusted arrival times = arrival_time - distance of bus stop
        self.arrival_times_adjusted = [p.arrival_time - p.bus_stop.distance for p in self.passengers]
        self.arrival_times_adjusted.sort()
    
    def _compute_prefix_sums(self, arr):
        prefix = [0]
        for v in arr:
            prefix.append(prefix[-1] + v)
        return prefix

    def _compute_group_costs(self):
        # Precompute cost to serve passengers from i to j with single bus departing at optimal time
        # cost(i,j) = sum of waiting times minimized by choosing bus departure time optimally
        # Optimal bus departure time corresponds to median of adjusted arrival times in [i,j]
        cost = [[0]* (self.n+1) for _ in range(self.n+1)]
        a = self.arrival_times_adjusted
        prefix = self._compute_prefix_sums(a)

        for i in range(1, self.n+1):
            for j in range(i, self.n+1):
                length = j - i + 1
                median_idx = i + (length - 1)//2
                median = a[median_idx-1]
                # sum of absolute differences from median
                left_count = median_idx - i
                right_count = j - median_idx
                left_sum = median * left_count - (prefix[median_idx-1] - prefix[i-1])
                right_sum = (prefix[j] - prefix[median_idx]) - median * right_count
                cost[i][j] = left_sum + right_sum
        self.cost = cost

    def minimize_total_waiting_time(self):
        self._preprocess_passengers()
        self._compute_group_costs()

        INF = 10**15
        dp = [[INF]*(self.n+1) for _ in range(self.m+1)]
        dp[0][0] = 0
        for k in range(1, self.m+1):
            # Divide passengers into k groups to minimize sum of waiting times
            # dp[k][j] = min over i<j of dp[k-1][i] + cost(i+1, j)
            opt = [0]*(self.n+1)
            def compute_dp(k, l, r, optl, optr):
                if l > r:
                    return
                mid = (l+r)//2
                best_i = -1
                best_val = INF
                start = optl
                end = min(mid-1, optr)
                for i in range(start, end+1):
                    val = dp[k-1][i] + self.cost[i+1][mid]
                    if val < best_val:
                        best_val = val
                        best_i = i
                dp[k][mid] = best_val
                opt[mid] = best_i
                compute_dp(k, l, mid-1, optl, best_i)
                compute_dp(k, mid+1, r, best_i, optr)
            compute_dp(k, 1, self.n, 0, self.n-1)
        return dp[self.m][self.n]

class InputOutputProcessor:
    def read_input(self):
        import sys
        s,n,m = map(int, sys.stdin.readline().strip().split())
        x_list = list(map(int, sys.stdin.readline().strip().split()))
        bus_stops = [BusStop(i+1, x) for i,x in enumerate(x_list)]
        passengers = []
        for _ in range(n):
            t_i, p_i = map(int, sys.stdin.readline().strip().split())
            passengers.append(Passenger(t_i, bus_stops[p_i-1]))
        return s, n, m, bus_stops, passengers

    def output_result(self, result):
        print(result)

class TiMeTableSolution:
    def run(self):
        io = InputOutputProcessor()
        s, n, m, bus_stops, passengers = io.read_input()
        route = BusRoute(bus_stops)
        optimizer = BusScheduleOptimizer(route, passengers, m)
        ans = optimizer.minimize_total_waiting_time()
        io.output_result(ans)

if __name__=="__main__":
    TiMeTableSolution().run()