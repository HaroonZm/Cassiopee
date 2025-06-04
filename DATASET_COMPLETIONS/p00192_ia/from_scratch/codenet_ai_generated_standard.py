import sys
input = sys.stdin.readline

class ParkingSpace:
    def __init__(self):
        self.upper = None  # (car_id, remaining_time)
        self.lower = None  # (car_id, remaining_time)

    def is_empty(self):
        return self.upper is None and self.lower is None

    def empty_spots(self):
        spots = 0
        if self.lower is None: spots += 1
        if self.upper is None: spots += 1
        return spots

    def add_car(self, car_id, time):
        # If empty, park lower
        if self.lower is None and self.upper is None:
            self.lower = [car_id, time]
            return 'lower'
        # If only lower present, park upper
        elif self.lower is not None and self.upper is None:
            self.upper = [car_id, time]
            return 'upper'
        # If lower empty but upper present -> park lower
        elif self.lower is None and self.upper is not None:
            self.lower = [car_id, time]
            return 'lower'
        # full
        return None

    def get_remaining_times(self):
        times = []
        if self.lower:
            times.append(self.lower[1])
        if self.upper:
            times.append(self.upper[1])
        return times

    def update_times(self, dt):
        if self.lower:
            self.lower[1] -= dt
        if self.upper:
            self.upper[1] -= dt

    def earliest_exit(self):
        # Returns list of cars with time <=0 to exit
        exits = []
        if self.lower and self.lower[1] <= 0:
            exits.append(('lower', self.lower[0]))
        if self.upper and self.upper[1] <= 0:
            exits.append(('upper', self.upper[0]))
        return exits

    def remove_car(self, position):
        if position == 'lower':
            self.lower = None
        elif position == 'upper':
            self.upper = None

def main():
    results = []
    while True:
        line = input()
        if not line:
            break
        m, n = map(int, line.split())
        if m == 0 and n == 0:
            break
        times = [int(input()) for _ in range(n)]

        parking = [ParkingSpace() for _ in range(m)]

        # arrival times every 10 minutes per car, id from 1
        # keep track of which cars are waiting to park
        waiting = []
        output_order = []
        time = 0
        car_idx = 0  # next arriving car

        # to simulate: at each event (car arrival or exit), process

        # We use a timeline and event driven simulation
        # Events:
        # 1) car arrives every 10 min until car_idx == n
        # 2) cars exit once their time is up

        # For efficiency track next arrival time = car_idx *10, and next exit time = min remaining times

        parked_cars = {} # car_id: (space_idx, slot: lower/upper)
        waiting_queue = []

        current_time = 0

        # To find next exit event time, we track the minimal remaining time + current_time
        def earliest_exit_time():
            min_time = None
            for sp in parking:
                for pos in ['lower', 'upper']:
                    c = getattr(sp,pos)
                    if c is not None:
                        exit_t = current_time + c[1]
                        if min_time is None or exit_t < min_time:
                            min_time = exit_t
            return min_time

        while len(output_order) < n:
            next_arrival_time = car_idx*10 if car_idx < n else None
            next_exit_time = earliest_exit_time()

            # next event time
            if next_arrival_time is None:
                next_event = next_exit_time
            elif next_exit_time is None:
                next_event = next_arrival_time
            else:
                next_event = min(next_arrival_time, next_exit_time)

            dt = next_event - current_time if next_event is not None else 0

            # update remaining time
            for sp in parking:
                sp.update_times(dt)

            current_time = next_event

            # process exits first if any
            # collect all cars that should exit at this time (<=0)
            exiting_cars = []
            for i, sp in enumerate(parking):
                exits = sp.earliest_exit()
                # for upper exit, check if lower present
                for pos, cid in exits:
                    exiting_cars.append((i, pos, cid))
            # sort by parking space number ascending
            exiting_cars.sort(key=lambda x: x[0])

            # process exits respecting rules
            # upper cars wait for lower to exit first
            # So first remove all lower cars that exit now in order
            lower_exits = [e for e in exiting_cars if e[1] == 'lower']
            for i,pos,cid in lower_exits:
                parking[i].remove_car(pos)
                output_order.append(cid)
                if cid in parked_cars: del parked_cars[cid]
            # then remove upper cars that can exit now if lower is gone
            upper_exits = [e for e in exiting_cars if e[1] == 'upper']
            for i,pos,cid in upper_exits:
                # cannot exit if lower still there
                if parking[i].lower is None:
                    parking[i].remove_car(pos)
                    output_order.append(cid)
                    if cid in parked_cars: del parked_cars[cid]

            # after exits at this time, try to park waiting cars if no parking space available previously
            def can_park(car_id):
                t = times[car_id-1]
                # find empty spaces (no cars)
                empty_spaces = [idx for idx, sp in enumerate(parking) if sp.is_empty()]
                if empty_spaces:
                    return min(empty_spaces)
                # find partially empty (one empty spot)
                partially_empty = [idx for idx, sp in enumerate(parking) if sp.empty_spots() > 0]
                if partially_empty:
                    return min(partially_empty)
                # if full parkings, apply rule of min dif
                difs = []
                for idx, sp in enumerate(parking):
                    # Each space has 1 or 2 cars
                    # For this rule: 
                    # if any car rem_time >= t: pick the min diff of those rem_time - t (>=0)
                    # else pick min diff of t - rem_time (<0)
                    remaints = []
                    if sp.lower: remaints.append(sp.lower[1])
                    if sp.upper: remaints.append(sp.upper[1])
                    rem_ge_t = [r for r in remaints if r >= t]
                    if rem_ge_t:
                        diff = min(r - t for r in rem_ge_t)
                        difs.append((diff, idx))
                    else:
                        diff = min(t - r for r in remaints)
                        difs.append((diff, idx))
                min_diff = min(difs, key=lambda x: (x[0], x[1]))[0]
                candidates = [idx for d, idx in difs if d == min_diff]
                return min(candidates)

            # park cars from waiting queue as priority
            while waiting_queue:
                c_id = waiting_queue[0]
                sp_idx = can_park(c_id)
                sp = parking[sp_idx]
                slot = sp.add_car(c_id, times[c_id-1])
                if slot is None:
                    # no space, break
                    break
                parked_cars[c_id] = (sp_idx, slot)
                waiting_queue.pop(0)

            # Then, if arrival at this moment, try park or wait
            if next_arrival_time is not None and next_arrival_time == current_time and car_idx < n:
                c_id = car_idx+1
                sp_idx = can_park(c_id)
                sp = parking[sp_idx]
                slot = sp.add_car(c_id, times[c_id-1])
                if slot is None:
                    waiting_queue.append(c_id)
                else:
                    parked_cars[c_id] = (sp_idx, slot)
                car_idx += 1

                # after arrival, try to park waiting cars as well
                while waiting_queue:
                    c_id = waiting_queue[0]
                    sp_idx = can_park(c_id)
                    sp = parking[sp_idx]
                    slot = sp.add_car(c_id, times[c_id-1])
                    if slot is None:
                        break
                    parked_cars[c_id] = (sp_idx, slot)
                    waiting_queue.pop(0)

        results.append(' '.join(map(str, output_order)))

    print('\n'.join(results))

if __name__ == '__main__':
    main()