class NinjaHouseExplorer:
    class Room:
        def __init__(self, id_, num_doors):
            self.id = id_
            self.num_doors = num_doors
            self.connections = []

        def connect(self, other):
            self.connections.append(other.id)

        def sorted_connections_str(self):
            conns = sorted(self.connections)
            return f"{self.id} " + " ".join(map(str, conns)) + f" {self.num_doors}"

    class ExplorationState:
        def __init__(self):
            self.rooms = []
            self.distance_map = {}  # room_id -> distance from first room
            self.id_map = {}        # distance -> room object
            self.current_room = None
            self.room_stack = []
            self.distance = 1

        def add_room(self, num_doors):
            new_id = len(self.rooms) + 1
            room = NinjaHouseExplorer.Room(new_id, num_doors)
            self.rooms.append(room)
            self.distance_map[new_id] = self.distance
            self.id_map[self.distance] = room
            return room

        def get_room_by_distance_diff(self, diff):
            # diff is negative
            curr_dist = self.distance
            target_dist = curr_dist + diff  # since diff < 0
            if target_dist not in self.id_map:
                raise ValueError(f"Invalid backward distance lookup: {target_dist}")
            return self.id_map[target_dist]

    def __init__(self, record):
        self.record = record
        self.state = NinjaHouseExplorer.ExplorationState()

    def reconstruct_graph(self):
        rec = self.record
        state = self.state
        # Begin exploration by creating first room with first positive number
        idx = 0
        first_doors = rec[idx]
        idx += 1
        first_room = state.add_room(first_doors)
        state.current_room = first_room
        state.room_stack.append(first_room)
        # We'll maintain for each room a "door pointer" index starting at 0 for the rightmost door
        # but since problem says "rightmost" we assume door order starts from rightmost door as 0, next left 1, etc.
        # To keep it general, we store for each room how many doors visited/opened so far.
        doors_opened = {r.id:0 for r in state.rooms}

        # The core loop processes the sequence rec from idx onward until termination (0)
        while idx < len(rec):
            x = rec[idx]
            idx += 1
            if x == 0:
                break
            if x > 0:
                # New room met through a door
                # Record number of doors = x for new room
                current_room = state.current_room
                # Increment door pointer for current room
                doors_opened[current_room.id] += 1
                new_room = state.add_room(x)
                # Create connection from current to new room, and from new room to current room
                current_room.connect(new_room)
                new_room.connect(current_room)
                # Descend into new room
                state.room_stack.append(new_room)
                state.current_room = new_room
                state.distance += 1
                doors_opened[new_room.id] = 0
            else:
                # Negative number: backward to an existing room
                current_room = state.current_room
                # Increment door pointer for current room (we tried a door but could not enter)
                doors_opened[current_room.id] += 1
                target_room = state.get_room_by_distance_diff(x)
                # Connect current room to target room (door that is being "closed" is connecting these rooms)
                # Because exploration says we skip door and close it, but it still connects rooms
                current_room.connect(target_room)
                target_room.connect(current_room)
                # We cannot go into target room, must return to previous room
                # Pop current room from stack, go back
                state.room_stack.pop()
                state.distance -= 1
                if not state.room_stack:
                    # Finished all rooms
                    break
                state.current_room = state.room_stack[-1]
        return state.rooms

def parse_input_records(lines):
    records = []
    current_record = []
    for line in lines:
        for num_str in line.strip().split():
            num = int(num_str)
            if num == 0:
                if current_record:
                    records.append(current_record)
                current_record = []
            else:
                current_record.append(num)
    if current_record:
        records.append(current_record)
    return records

def process_and_output(records):
    results = []
    for record in records:
        exp = NinjaHouseExplorer(record)
        rooms = exp.reconstruct_graph()
        # Output rooms lines as requested: ordered by room id, connections ascending order, format:
        # i r1 r2 ... r_k_i k_i
        # But problem states line j-th line is that for room j, so output in order of id
        output_lines = []
        for room in rooms:
            output_lines.append(room.sorted_connections_str())
        results.append(output_lines)
    return results

def main():
    import sys
    input_lines = sys.stdin.readlines()
    n = int(input_lines[0].strip())
    records = parse_input_records(input_lines[1:])
    # It might be more records than n read, but problem states n records at most
    records = records[:n]
    results = process_and_output(records)
    for i, res in enumerate(results):
        for line in res:
            print(line)

if __name__ == "__main__":
    main()