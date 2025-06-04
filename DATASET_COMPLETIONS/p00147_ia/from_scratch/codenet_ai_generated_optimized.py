import sys
from collections import deque

def main():
    seats_num = 17
    groups_num = 100
    groups = []
    for i in range(groups_num):
        arrival = 5 * i
        size = 5 if i % 5 == 1 else 2
        eat = 17 * (i % 2) + 3 * (i % 3) + 19
        groups.append((arrival, size, eat))

    input_lines = sys.stdin.read().strip().split('\n')
    queries = list(map(int, input_lines))

    # We simulate once all groups arrival and seating to get each group's wait time
    # Simulation variables
    time = 0
    seats = [-1] * seats_num
    queue = deque()
    group_end_times = [-1] * groups_num
    wait_times = [-1] * groups_num

    arrived_idx = 0  # next group to arrive
    seated_count = 0  # number of seated groups
    eating_groups = {}  # group_id -> end_time

    # Helper function to find seating position for group size x
    def find_seats(x):
        count = 0
        start = 0
        for i in range(seats_num):
            if seats[i] == -1:
                count += 1
            else:
                count = 0
                start = i + 1
            if count == x:
                return start
        return -1

    # We know last group's finishing time at most is:
    max_time = groups[-1][0] + max(g[2] for g in groups) + 1

    while seated_count < groups_num:
        # Process groups finishing eating at this time and free seats
        finished = [gid for gid, endt in eating_groups.items() if endt == time]
        for gid in finished:
            # Free seats of group gid
            size = groups[gid][1]
            # find and free these seats
            # They occupy a consecutive block of seats, unique per group
            # We can find by scanning seats for gid
            idx = 0
            while idx < seats_num:
                if seats[idx] == gid:
                    for j in range(idx, idx + size):
                        seats[j] = -1
                    break
                idx += 1
            del eating_groups[gid]

        # Advance arrival: add newly arrived groups to queue or seat directly if possible and queue empty
        while arrived_idx < groups_num and groups[arrived_idx][0] == time:
            size = groups[arrived_idx][1]
            if not queue:
                pos = find_seats(size)
                if pos != -1:
                    # seat them immediately
                    for j in range(pos, pos + size):
                        seats[j] = arrived_idx
                    eating_groups[arrived_idx] = time + groups[arrived_idx][2]
                    wait_times[arrived_idx] = 0
                    seated_count += 1
                else:
                    queue.append(arrived_idx)
            else:
                queue.append(arrived_idx)
            arrived_idx += 1

        # Try to seat queue groups as many as possible in order
        while queue:
            gid = queue[0]
            size = groups[gid][1]
            pos = find_seats(size)
            if pos == -1:
                break
            # seat group
            for j in range(pos, pos + size):
                seats[j] = gid
            eating_groups[gid] = time + groups[gid][2]
            wait_times[gid] = time - groups[gid][0]
            seated_count += 1
            queue.popleft()

        time += 1
        if time > max_time + 1000:
            # safety stop, should not happen
            break

    for q in queries:
        print(wait_times[q])

if __name__ == "__main__":
    main()