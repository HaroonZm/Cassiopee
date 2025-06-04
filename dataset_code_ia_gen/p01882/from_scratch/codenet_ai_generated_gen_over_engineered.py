class Member:
    __slots__ = ['name', 'motivation', 'join_order']

    def __init__(self, name: str, motivation: int, join_order: int):
        self.name = name
        self.motivation = motivation
        self.join_order = join_order

    def key(self):
        # Higher motivation ranks higher, if tie, later join_order ranks higher
        # We invert join_order for the "later joined higher" priority
        return (-self.motivation, -self.join_order)

class WorkstyleManager:
    def __init__(self):
        # member_name -> Member instance
        self.members = {}
        # All active members ranked by motivation and join date (descending)
        self.sorted_members = []
        # We keep workhorse and idle fellows sets (by member name)
        self.workhorses = set()
        self.idle_fellows = set()
        self.logs = []
        self.join_counter = 0

    def _binary_search_insert_pos(self, member_key):
        # Binary search to find insert position in sorted_members by key
        lo, hi = 0, len(self.sorted_members)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.sorted_members[mid].key() < member_key:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def _insert_member(self, member):
        pos = self._binary_search_insert_pos(member.key())
        self.sorted_members.insert(pos, member)

    def _remove_member(self, member):
        # Binary search by key and find by identity
        key = member.key()
        lo, hi = 0, len(self.sorted_members)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.sorted_members[mid].key() < key:
                hi = mid
            elif self.sorted_members[mid].key() > key:
                lo = mid + 1
            else:
                # Key equals, search neighbors for exact member (name)
                # Because multiple members could have same key (motivation and join_order), but join_order unique ensures unique key here
                # So one candidate:
                if self.sorted_members[mid].name == member.name:
                    self.sorted_members.pop(mid)
                    return
                # Not found, but must be no duplicate keys because join_order unique
                break
        # In case not found, fallback linear search (safe but slow)
        for i, m in enumerate(self.sorted_members):
            if m.name == member.name:
                self.sorted_members.pop(i)
                break

    def _current_top_count(self):
        return (len(self.sorted_members) * 20) // 100

    def _reevaluate_workstyles(self):
        top_count = self._current_top_count()
        new_workhorses = set()
        for i in range(top_count):
            new_workhorses.add(self.sorted_members[i].name)
        new_idle = set(m.name for m in self.sorted_members[top_count:])

        # Detect changes and log
        # Members newly in workhorses but previously idle:
        for nm in new_workhorses:
            if nm not in self.workhorses:
                self.logs.append(f"{nm} is working hard now.")
        # Members newly idle but previously workhorses:
        for nm in new_idle:
            if nm in self.workhorses:
                self.logs.append(f"{nm} is not working now.")

        self.workhorses = new_workhorses
        self.idle_fellows = new_idle

    def initial_load(self, initial_members):
        # initial_members is list of tuples (name, motivation)
        for nm, mot in initial_members:
            m = Member(nm, mot, self.join_counter)
            self.join_counter += 1
            self.members[nm] = m
            self._insert_member(m)
        # Initial workstyle determination
        # Actually, no initial logging is needed. Only changes after each event.
        self._reevaluate_workstyles()

    def process_event(self, event: str):
        # return True if logs happened, else False
        parts = event.split()
        if parts[0] == '+':
            # Incoming member: + name motivation
            name = parts[1]
            motivation = int(parts[2])
            m = Member(name, motivation, self.join_counter)
            self.join_counter += 1
            self.members[name] = m
            self._insert_member(m)
            # New member either workhorse or idle immediately, then adjust others
            self._reevaluate_workstyles()
            # Print log for the member's initial workstyle
            if name in self.workhorses:
                self.logs.append(f"{name} is working hard now.")
            else:
                self.logs.append(f"{name} is not working now.")
            # _reevaluate_workstyles added changes for others too.
            return True
        else:
            # Outgoing member: - name
            name = parts[1]
            if name not in self.members:
                # Ignore non-existing
                return False
            member = self.members.pop(name)
            was_workhorse = name in self.workhorses
            self._remove_member(member)
            self._reevaluate_workstyles()
            # No log for leaving member itself
            # Only changes for transitions of others possibly logged from _reevaluate_workstyles
            return True

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    initial_members = []
    for _ in range(N):
        s, a = input().rstrip('\n').split()
        a = int(a)
        initial_members.append((s, a))
    M = int(input())
    events = [input().rstrip('\n') for _ in range(M)]

    manager = WorkstyleManager()
    manager.initial_load(initial_members)

    # No initial log output for startup (per samples)
    # Outputs only changes after each event

    for event in events:
        # Save old logs count to isolate new logs per event in order
        old_count = len(manager.logs)
        manager.process_event(event)
        # Print new logs after event in chronological order
        for log in manager.logs[old_count:]:
            print(log)

if __name__ == "__main__":
    main()