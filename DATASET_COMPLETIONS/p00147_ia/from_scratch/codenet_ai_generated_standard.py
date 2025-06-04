import sys

class Group:
    def __init__(self, i):
        self.i = i
        self.arrival = 5 * i
        self.size = 5 if i % 5 == 1 else 2
        self.dining = 17 * (i % 2) + 3 * (i % 3) + 19
        self.seated_time = None

def find_seats(seats, size):
    count = 0
    start = 0
    for i, s in enumerate(seats):
        if s == -1:
            if count == 0: start = i
            count += 1
            if count == size:
                return start
        else:
            count = 0
    return None

def simulate(groups):
    seats = [-1] * 17
    time = 0
    queue = []
    finished = set()
    seating_end_times = []
    i = 0
    max_time = 5 * 99 + max(g.dining for g in groups)
    while i < 100 or queue or seating_end_times:
        # free seats
        seats_to_free = [t for t in seating_end_times if t[0] == time]
        for _, gidx, seat_start, size in seats_to_free:
            for pos in range(seat_start, seat_start+size):
                seats[pos] = -1
            finished.add(gidx)
        seating_end_times = [t for t in seating_end_times if t[0] != time]

        # add arriving groups
        while i < 100 and groups[i].arrival == time:
            if queue:
                queue.append(i)
            else:
                pos = find_seats(seats, groups[i].size)
                if pos is None:
                    queue.append(i)
                else:
                    for p in range(pos,pos+groups[i].size):
                        seats[p] = i
                    groups[i].seated_time = time
                    seating_end_times.append((time+groups[i].dining, i, pos, groups[i].size))
            i += 1

        # seat groups in queue
        while queue:
            front = queue[0]
            pos = find_seats(seats, groups[front].size)
            if pos is None:
                break
            for p in range(pos,pos+groups[front].size):
                seats[p] = front
            groups[front].seated_time = time
            seating_end_times.append((time+groups[front].dining, front, pos, groups[front].size))
            queue.pop(0)

        time += 1
        if time > max_time and not queue and not seating_end_times:
            break

n_values = [int(line) for line in sys.stdin.read().strip().split()]
groups = [Group(i) for i in range(100)]
simulate(groups)
for n in n_values:
    wait = (groups[n].seated_time - groups[n].arrival) if groups[n].seated_time is not None else 0
    print(max(wait,0))