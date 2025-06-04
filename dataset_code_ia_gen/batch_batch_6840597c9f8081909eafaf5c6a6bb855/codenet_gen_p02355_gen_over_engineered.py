class FrequencyMap:
    def __init__(self):
        self._freq = {}
    
    def increment(self, key):
        self._freq[key] = self._freq.get(key, 0) + 1
    
    def decrement(self, key):
        if key in self._freq:
            self._freq[key] -= 1
            if self._freq[key] == 0:
                del self._freq[key]
    
    def contains_all(self, required_keys):
        # Check if all keys in required_keys are present in self._freq
        return all(key in self._freq for key in required_keys)
    
    def count_keys(self):
        return len(self._freq)


class Window:
    def __init__(self, array, required_elements):
        self.array = array
        self.required_elements = required_elements
        self.freq_map = FrequencyMap()
        self.left = 0
        self.right = -1
        self.covered = 0
        self.required_count = len(required_elements)
        self.required_freq = {key:1 for key in required_elements}
    
    def add_right(self):
        self.right += 1
        if self.right < len(self.array):
            val = self.array[self.right]
            if val in self.required_freq:
                prev_count = self.freq_map._freq.get(val, 0)
                self.freq_map.increment(val)
                if prev_count < self.required_freq[val] and self.freq_map._freq[val] >= self.required_freq[val]:
                    self.covered += 1
            return True
        return False
    
    def remove_left(self):
        if self.left <= self.right and self.left < len(self.array):
            val = self.array[self.left]
            if val in self.required_freq:
                if self.freq_map._freq.get(val, 0) == self.required_freq[val]:
                    self.covered -= 1
                self.freq_map.decrement(val)
            self.left += 1
    
    def contains_all_required(self):
        return self.covered == self.required_count
    
    def current_window_size(self):
        return self.right - self.left + 1


class SmallestWindowFinder:
    def __init__(self, array, K):
        self.array = array
        self.K = K
        self.required_elements = list(range(1, K+1))
    
    def find_smallest_window_size(self):
        if self.K == 0:
            return 0
        window = Window(self.array, self.required_elements)
        min_size = float('inf')
        while window.add_right():
            while window.contains_all_required():
                current_size = window.current_window_size()
                if current_size < min_size:
                    min_size = current_size
                window.remove_left()
        return 0 if min_size == float('inf') else min_size


def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    N, K = map(int, input_data[0:2])
    array = list(map(int, input_data[2:2+N]))
    finder = SmallestWindowFinder(array, K)
    print(finder.find_smallest_window_size())

if __name__ == "__main__":
    main()