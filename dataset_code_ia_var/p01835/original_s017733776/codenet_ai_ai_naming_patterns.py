import sys

class CoherentSet:
    __slots__ = ["tree_data", "freq_data", "max_index", "tree_base", "elem_count"]

    def __init__(self, max_size):
        self.tree_data = [0] * (max_size + 1)
        self.freq_data = [0] * (max_size + 1)
        self.max_index = max_size
        self.tree_base = 2 ** (max_size.bit_length() - 1)
        self.elem_count = 0

    def _prefix_sum(self, idx):
        result = 0
        arr = self.tree_data
        while idx:
            result += arr[idx]
            idx -= idx & -idx
        return result

    def _update(self, idx, delta):
        n = self.max_index
        self.freq_data[idx] += delta
        arr = self.tree_data
        while idx <= n:
            arr[idx] += delta
            idx += idx & -idx
        self.elem_count += delta

    def _find_kth(self, target):
        curr_sum = 0
        idx = 0
        step = self.tree_base
        n = self.max_index
        arr = self.tree_data
        while step:
            if idx + step <= n and curr_sum + arr[idx + step] <= target:
                curr_sum += arr[idx + step]
                idx += step
            step >>= 1
        return idx

    def insert(self, key, count=1):
        self._update(key + 1, count)

    def erase(self, key, count=1):
        self._update(key + 1, -count)

    def position(self, key):
        if self.freq_data[key + 1] == 0:
            return -1
        return self._prefix_sum(key + 1)

    def __contains__(self, key):
        return self.freq_data[key + 1] > 0

    def __iter__(self):
        key = self.successor(0)
        n = self.max_index
        while key < n:
            for _ in range(self.freq_data[key + 1]):
                yield key
            key = self.successor(key + 1)

    def frequency(self, key):
        return self.freq_data[key + 1]

    def __len__(self):
        return self.elem_count

    def predecessor(self, key):
        val = self._prefix_sum(key + 1) - self.freq_data[key + 1] - 1
        if val == -1:
            return -1
        return self._find_kth(val)

    def successor(self, key):
        if key == self.max_index or self.freq_data[key + 1]:
            return key
        val = self._prefix_sum(key + 1)
        return self._find_kth(val)

    def by_order(self, order):
        return self._find_kth(order)

    def __getitem__(self, order):
        return self._find_kth(order)

def coherent_solve():
    stdin_read = sys.stdin.readline
    stdout_write = sys.stdout.write

    num_positions, required_count = map(int, stdin_read().split())
    num_intervals = int(stdin_read())
    interval_starts = [[] for _ in range(num_positions + 1)]
    interval_ends = [[] for _ in range(num_positions + 1)]
    interval_values = [0] * num_intervals
    active_set = CoherentSet(num_intervals)
    for idx in range(num_intervals):
        left, right, value = map(int, stdin_read().split())
        interval_starts[left - 1].append(idx)
        interval_ends[right].append(idx)
        interval_values[idx] = value
    component_count = 0
    answer = 0
    for pos in range(num_positions):
        for k in interval_starts[pos]:
            active_set.insert(k)
            prev_idx = active_set.predecessor(k)
            next_idx = active_set.successor(k + 1)
            if prev_idx != -1 and next_idx < num_intervals:
                if interval_values[prev_idx] + 1 == interval_values[next_idx]:
                    component_count -= 1
            if prev_idx != -1:
                if interval_values[prev_idx] + 1 == interval_values[k]:
                    component_count += 1
            if next_idx < num_intervals:
                if interval_values[k] + 1 == interval_values[next_idx]:
                    component_count += 1
        for k in interval_ends[pos]:
            active_set.erase(k)
            prev_idx = active_set.predecessor(k)
            next_idx = active_set.successor(k + 1)
            if prev_idx != -1:
                if interval_values[prev_idx] + 1 == interval_values[k]:
                    component_count -= 1
            if next_idx < num_intervals:
                if interval_values[k] + 1 == interval_values[next_idx]:
                    component_count -= 1
            if prev_idx != -1 and next_idx < num_intervals:
                if interval_values[prev_idx] + 1 == interval_values[next_idx]:
                    component_count += 1
        if len(active_set) == required_count and component_count == required_count - 1:
            answer += 1
    stdout_write("%d\n" % answer)

coherent_solve()