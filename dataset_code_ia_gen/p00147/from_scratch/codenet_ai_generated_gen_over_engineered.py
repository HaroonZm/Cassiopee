class Group:
    def __init__(self, index: int):
        self.index = index
        self.arrival = 5 * index
        self.size = 5 if index % 5 == 1 else 2
        self.eat_time = 17 * (index % 2) + 3 * (index % 3) + 19
        self.wait = 0
        self.seated_time = None
        self.seat_start = None

    def __repr__(self):
        return f"G{self.index}(arr={self.arrival}, size={self.size}, eat={self.eat_time})"


class Seating:
    def __init__(self, seats_count: int = 17):
        self.seats_count = seats_count
        self.seats = [None] * self.seats_count  # None or Group index seated

    def can_seat(self, group: Group) -> int:
        # Find first block of consecutive free seats of length group.size
        count = 0
        for i in range(self.seats_count):
            if self.seats[i] is None:
                count += 1
                if count == group.size:
                    return i - group.size + 1
            else:
                count = 0
        return -1

    def seat_group(self, group: Group, start_pos: int, current_time: int):
        for i in range(start_pos, start_pos + group.size):
            self.seats[i] = group.index
        group.seated_time = current_time
        group.seat_start = start_pos

    def leave_group(self, group: Group):
        for i in range(group.seat_start, group.seat_start + group.size):
            self.seats[i] = None

    def __repr__(self):
        # Represent seats: '_' for empty, else group index modulo 10
        return ''.join(str(s % 10) if s is not None else '_' for s in self.seats)


class QueueSystem:
    def __init__(self, total_groups: int = 100):
        self.groups = [Group(i) for i in range(total_groups)]
        self.seating = Seating()
        self.current_time = 0
        self.wait_queue = []
        self.occupied_groups = []
        self.last_arrived = 0  # index of last group arrived
        self.max_group_index = total_groups - 1
        self.events = []  # (time, 'arrive', group_index) or (time, 'leave', group_index)

    def run_until(self, target_index: int):
        # We simulate forward until group[target_index] is seated
        # or beyond seating time of all groups <= target_index
        groups = self.groups
        wait_queue = self.wait_queue
        seating = self.seating
        occupied_groups = self.occupied_groups

        # Event-driven approach with per-minute increments per problem statement
        # We will keep track of next arrivals and next leaves by time
        last_time = 0

        # Prepare tracking structure: we need to know when groups must arrive
        arrivals = {g.arrival: [] for g in groups}
        for g in groups:
            arrivals[g.arrival].append(g)

        # Map group index to leave time if seated: seated_time + eat_time

        # We simulate by time starting from 0 and incrementing by 1 until conditions met
        time = 0
        seated_groups = set()
        seated_target = False

        while True:
            # 1. Handle leaving groups at time
            leaving_groups_now = [g for g in occupied_groups if g.seated_time + g.eat_time == time]
            if leaving_groups_now:
                # Groups leave simultaneously at beginning of this minute
                for g in leaving_groups_now:
                    seating.leave_group(g)
                for g in leaving_groups_now:
                    occupied_groups.remove(g)

            # 2. Handle arriving groups at time
            if time in arrivals:
                for g in arrivals[time]:
                    # Decide to seat or queue
                    if not wait_queue:  # no queue yet
                        # Attempt seating immediately
                        start_pos = seating.can_seat(g)
                        if start_pos != -1:
                            seating.seat_group(g, start_pos, time)
                            occupied_groups.append(g)
                            if g.index == target_index:
                                seated_target = True
                        else:
                            # Queue because no seat
                            wait_queue.append(g)
                    else:
                        # Queue always because a queue exists
                        wait_queue.append(g)

            # 3. Try to seat from queue as many groups as possible in order, without skipping
            # If wait_queue empty then skip
            if wait_queue:
                # We try to seat from the first group in queue as many as possible in order,
                # but if first can't seat no one seats
                while wait_queue:
                    first = wait_queue[0]
                    start_pos = seating.can_seat(first)
                    if start_pos == -1:
                        # No seating possible for first, stop seating attempts for others
                        break
                    else:
                        seating.seat_group(first, start_pos, time)
                        occupied_groups.append(first)
                        wait_queue.pop(0)
                        if first.index == target_index:
                            seated_target = True

            # If we seated target group and it has seated_time assigned, we can stop next minute
            # Wait time = seated_time - arrival_time
            if seated_target:
                break

            # Corner: if time goes beyond some large limit we stop to avoid infinite loops
            if time > 5 * self.max_group_index + 500:
                # Should never reach here logically, but just a safeguard
                break

            time += 1

        # Calculate wait time
        target_group = groups[target_index]
        wait_time = target_group.seated_time - target_group.arrival
        return wait_time


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    qs = QueueSystem()
    for line in input_lines:
        if not line.strip():
            continue
        n = int(line)
        wait = qs.run_until(n)
        print(wait)

if __name__ == "__main__":
    main()