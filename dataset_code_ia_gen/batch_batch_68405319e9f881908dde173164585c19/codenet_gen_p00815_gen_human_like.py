def solve():
    import sys
    sys.setrecursionlimit(10**7)

    input_lines = sys.stdin.read().strip().split()
    n = int(input_lines[0])

    idx = 1

    for _ in range(n):
        record = []
        while True:
            if idx >= len(input_lines):
                break
            x = int(input_lines[idx])
            idx += 1
            if x == 0:
                break
            record.append(x)

        # We'll rebuild the graph from record.

        # Each room numbered as visited order (1-based)
        # Keep track of:
        # - g: adjacency list map room->list of neighbors (with duplicates for multiple doors)
        # - room_doors: number of doors in each room
        # - distance: distance from first room (depth in exploration)
        # Exploration rules:
        # - We simulate the traversal, but we only have record[].
        # - record[i] > 0 means it is number of doors of the next new room
        # - record[i] < 0 means a back edge to an already visited room whose distance is known
        #
        # We need to reconstruct rooms and edges.

        # The approach:
        # We keep a stack of current path rooms:
        # stack = list of (room_id, doors_count)
        # We know first room has record[0] doors
        # We keep track of door usage index per room to map the order
        # For each record in record:
        #   if positive:
        #       new room arrives
        #       connect with door from current top of stack room
        #       push new room onto stack
        #       distance increments by 1
        #   else:
        #       negative means door to previously visited room:
        #       distance difference = record[i]
        #       from difference, find the room on stack with distance = current_distance + diff
        #       connect current room with that room
        # After exploring all doors, pop to back

        # Data structures
        g = dict()  # room_id -> list of connected room_ids (repeat for multiple doors)
        distance = dict()  # room_id -> distance from first room
        doors_count = dict()  # room_id -> number of doors
        visited_room_of_distance = dict() # distance -> room_id

        stack = []
        cur_room = 1
        cur_dist = 0

        pos = 0
        total_len = len(record)

        doors_count[cur_room] = record[0]
        distance[cur_room] = 0
        visited_room_of_distance[0] = cur_room
        g[cur_room] = []
        # For each room we'll need to know how many doors have been "tried" to open
        # to know when to backtrack
        door_used = dict()
        door_used[cur_room] = 0

        stack.append(cur_room)

        cur_room_id = cur_room
        cur_dist = 0

        pos = 1
        next_room_id = 2  # assign room ids incrementally as we discover new rooms

        # We'll use a list to know doors count per room:
        # rooms_doors[room_id] = number of doors in that room
        # but we have already doors_count, ok

        while pos < total_len:
            record_val = record[pos]
            pos += 1
            current_room = stack[-1]
            if record_val > 0:
                # new room
                new_room = next_room_id
                next_room_id += 1
                # connect current_room and new_room by door:
                g.setdefault(current_room, []).append(new_room)
                g.setdefault(new_room, []).append(current_room)
                # set distance and doors count for new room
                doors_count[new_room] = record_val
                distance[new_room] = distance[current_room] + 1
                visited_room_of_distance[distance[new_room]] = new_room
                g.setdefault(new_room, [])
                door_used[new_room] = 0
                # enter new room
                stack.append(new_room)
            else:
                # negative record: difference of the distance between an already visited room and current room
                diff = record_val
                target_distance = distance[stack[-1]] + diff
                target_room = visited_room_of_distance[target_distance]

                # connect current_room to target_room by a door
                g.setdefault(stack[-1], []).append(target_room)
                g.setdefault(target_room, []).append(stack[-1])
                # Since this door points to visited room, we don't enter it.
                # But we have "opened" this door, continue to next door
                # If all doors examined, backtrack
                door_used[stack[-1]] += 1
                if door_used[stack[-1]] == doors_count[stack[-1]]:
                    stack.pop()
                # If door_used < doors_count, do nothing, continue processing next record

                # continue to next record

            # When new room is entered (record_val>0), reset door usage for that room
            if record_val > 0:
                # After pushing new room, no door used yet for it - already initialized
                # For previous room, increment door_used by 1 (we used one door)
                # Rightmost door was used for entering new room: increment door used for previous room
                prev_room = stack[-2]
                door_used[prev_room] += 1
                # check if prev_room door_used == doors_count: if so pop
                while stack and door_used[stack[-1]] == doors_count[stack[-1]]:
                    stack.pop()
                    if stack:
                        door_used[stack[-1]] += 1
                    else:
                        break

        # printing output:
        # Number of rooms is max room id assigned (next_room_id-1)
        m = next_room_id - 1
        # For i in 1..m print:
        # i r1 r2 ... rk ki
        # r1 ..rk sorted ascending, duplicates preserved
        for i in range(1, m+1):
            neighbors = g.get(i, [])
            neighbors_sorted = sorted(neighbors)
            print(i, *neighbors_sorted, doors_count[i])