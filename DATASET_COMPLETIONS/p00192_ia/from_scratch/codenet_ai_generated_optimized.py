import sys
input = sys.stdin.readline

class ParkingSpace:
    def __init__(self, idx):
        self.idx = idx
        self.up = None    # (car_id, remaining_time)
        self.down = None  # (car_id, remaining_time)
    def empty(self):
        return self.up is None and self.down is None
    def has_empty(self):
        return self.up is None or self.down is None
    def min_remaining(self):
        times = []
        if self.up is not None:
            times.append(self.up[1])
        if self.down is not None:
            times.append(self.down[1])
        return min(times) if times else None
    def max_remaining(self):
        times = []
        if self.up is not None:
            times.append(self.up[1])
        if self.down is not None:
            times.append(self.down[1])
        return max(times) if times else None
    def cars(self):
        res = []
        if self.down is not None:
            res.append(self.down)
        if self.up is not None:
            res.append(self.up)
        return res

def main():
    while True:
        m, n = map(int,input().split())
        if m == 0 and n == 0:
            break
        t = [int(input()) for _ in range(n)]

        # Initialize parking spaces
        spaces = [ParkingSpace(i+1) for i in range(m)]

        # Each car arrives at time i*10
        time_now = 0
        waiting = []  # queue of (car_id, parking_time)
        parked = []   # list of (car_id, space_idx, up/down, exit_time)
        # up/down: 'up' or 'down'

        # State of parking spaces: up and down stores (car_id, remaining_time)
        # remaining_time is time left from current time

        # For simulating exit, we maintain a time line of events
        # But we simulate step by step at each arrival or departure time.

        # We will keep simulation in order of minute steps but that can be inefficient
        # Instead, since arrivals every 10 minutes, and all cars have parking time at arrival,
        # we can keep track of end times accordingly.

        # We simulate from first car arrival (time 0) and progress forward:
        # We maintain a set of cars currently parked with their exit times (absolute),
        # and cars waiting to park.

        # The challenge:
        # - when a car arrives, first remove cars that should have exited already,
        #   output in order the cars leaving at same time in ascending space number.
        # - then try to park the waiting cars and the new arrival cars in order

        # We maintain a current_time variable and process cars in chronological order.

        # We prepare data structure for parked cars:
        # per space, store (up_car_id, up_exit_time), (down_car_id, down_exit_time)
        # If no car, store None

        # For each car, arrival_time = i*10, exit_time = arrival_time + t[i]

        arrival_times = [i*10 for i in range(n)]
        exit_orders = []

        idx_next_car = 0
        waiting = []
        parked_info = [None]*(n+1)  # store (space_idx, 'up' or 'down') for car_id
        # Parking simulation loop by event
        # Events: car arrival or car exit
        # We maintain a min-heap for upcoming exit times for up and down cars per space
        import heapq

        # We'll have event queue [{time, type, car_id, space_idx, up/down}]
        # But since cars exit only at exit times, and arrive every 10 min,
        # we can simulate time by earliest event

        # Initialize parking space status
        # For simplicity, store for each space slot:
        # up: (car_id, exit_time) or None
        # down: (car_id, exit_time) or None
        for s in spaces:
            s.up = None
            s.down = None

        # We maintain:
        # wait_queue: list of cars waiting in order of arrival (car_id)
        wait_queue = []
        # cars not yet arrived:idx_next_car

        # For exiting cars, at an exit time:
        # - For up car, must wait for down car to leave first (if any)
        # - If down car exit time <= up car exit time, up can leave immediately after down
        # For output, must output cars in order of exit time and space idx

        # We can maintain a timeline of exit events:
        # But we need to simulate in order:
        # At each event time (arrival or exit), we first remove exited cars

        # Precalculate absolute exit times:
        abs_exit_times = [arrival_times[i]+t[i] for i in range(n)]

        # A list of events time points: all arrival times and all exit times
        # But exit can be delayed (for up if down not gone)

        # We'll simulate time in increasing order of events (arrival or exit), 
        # and handle all events at that time.

        # To do efficiently, we must know next event time.

        # So we maintain a min heap of exit events:
        # each item: (exit_time, space_idx, 'down' or 'up', car_id)
        exit_heap = []

        cars_parked_cnt = 0

        def remaining_times_per_space():
            res = []
            for s in spaces:
                vals = []
                if s.up:
                    vals.append(s.up[1]-time_now)
                if s.down:
                    vals.append(s.down[1]-time_now)
                if vals:
                    res.append(min(vals))
                else:
                    res.append(None)
            return res

        # At start time 0, process arrivals and events
        # Helper functions:

        def car_exit_all_possible(current_time):
            # Remove cars whose exit_time <= current_time
            # Output their car_ids in order of exit_time then space_idx
            # Return list of exited cars in order
            res = []
            while exit_heap and exit_heap[0][0] <= current_time:
                etime, sidx, pos, cid = heapq.heappop(exit_heap)
                space = spaces[sidx-1]
                # For up pos, must check if down left
                if pos == 'up':
                    # if down still parked, reinsert event after down leaves
                    if space.down is not None:
                        # push back to heap with same exit time but wait
                        # but we must delay exit until down gone
                        # we delay exit event until down leaves
                        continue
                    # else up can leave now
                    if space.up and space.up[0] == cid:
                        res.append(cid)
                        space.up = None
                else:
                    # down car can leave immediately
                    if space.down and space.down[0] == cid:
                        res.append(cid)
                        space.down = None
                        # After down leaves, if up waiting to leave, push up exit now
                        if space.up:
                            up_cid, up_et = space.up
                            # check if exists exit event for that up
                            # Add exit event immediately now (current_time)
                            heapq.heappush(exit_heap,(current_time, sidx, 'up', up_cid))
            return sorted(res, key=lambda x: parked_info[x][0])

        def park_car(car_id):
            ptime = t[car_id-1]
            # 1) check for empty spaces (no car at all)
            empty_spaces = [s for s in spaces if s.empty()]
            if empty_spaces:
                # Pick smallest idx space, goes to down position
                sp = empty_spaces[0]
                sp.down = (car_id, time_now+ptime)
                parked_info[car_id] = (sp.idx,'down')
                heapq.heappush(exit_heap,(time_now+ptime, sp.idx, 'down', car_id))
                return True
            # 2) check spaces with empty spot (one car parked)
            empty_spots = [s for s in spaces if s.has_empty()]
            # Remove those that are empty above (case 1)
            empty_spots = [s for s in empty_spots if not s.empty()]
            if empty_spots:
                # Decide which to pick by rules:
                # For each space, compute difference vs this ptime
                diffs = []
                for s in empty_spots:
                    # get last remaining parking time in space (min or max? rules say "残り駐車時間" so car parked)
                    rtimes = []
                    if s.up:
                        rtimes.append(s.up[1]-time_now)
                    if s.down:
                        rtimes.append(s.down[1]-time_now)
                    min_rtime = min(rtimes)
                    max_rtime = max(rtimes)
                    # If any remaining_time >= ptime: choose that with minimal difference >=0
                    # else difference < 0 minimal in magnitude
                    if any(rt >= ptime for rt in rtimes):
                        min_diff = min((rt - ptime for rt in rtimes if rt >= ptime))
                        diffs.append((min_diff, s.idx, s))
                    else:
                        min_diff = min((ptime - rt for rt in rtimes))
                        diffs.append((min_diff, s.idx, s))
                diffs.sort(key=lambda x: (x[0], x[1]))
                sp = diffs[0][2]
                # Must park new car on upper position
                # The previous car(s) must already be down or up
                # The problem states:
                # new car must be placed upper => existing car moves down (or is down)
                # According to example, older car goes down, new one goes up
                # So existing car moves down, new car goes up
                if sp.down is not None:
                    # existing down car remains
                    pass
                if sp.up is None:
                    # previous up car?
                    # According to problem, new car must go up, existing car is moved down
                    # But if up is none, previously only down car(s)
                    # So we must move down car to down position, new car to up position
                    old_down = sp.down
                    sp.down = old_down
                    sp.up = (car_id, time_now+ptime)
                    parked_info[car_id] = (sp.idx,'up')
                    heapq.heappush(exit_heap,(time_now+ptime, sp.idx, 'up', car_id))
                    # The existing car goes down, must update remaining time
                    # It stays same time, but no event to change, its exit event remains.
                    return True
            # 3) no space available
            return False

        # Simulation loop
        # Each time point is arrival time of a car, or exit event time
        # We take next earliest event among:
        # - next car arrival if idx_next_car < n
        # - next exit event if exit_heap not empty

        output_order = []

        while idx_next_car<n or exit_heap or wait_queue:
            next_arrival = arrival_times[idx_next_car] if idx_next_car<n else float("inf")
            next_exit = exit_heap[0][0] if exit_heap else float("inf")
            time_now = min(next_arrival, next_exit)

            # 1) first remove all cars exited at or before time_now
            exited_cars = car_exit_all_possible(time_now)
            output_order.extend(exited_cars)

            # 2) process all cars arriving at this time_now
            while idx_next_car<n and arrival_times[idx_next_car]==time_now:
                wait_queue.append(idx_next_car+1)
                idx_next_car+=1

            # 3) park as many waiting cars as possible in order
            changed = True
            while wait_queue and changed:
                changed = False
                # attempt to park first waiting car
                car_id = wait_queue[0]
                if park_car(car_id):
                    wait_queue.pop(0)
                    changed = True

            # if no event and no arrival, break
            if next_arrival==float("inf") and next_exit==float("inf"):
                break

        print(*output_order)

if __name__ == "__main__":
    main()