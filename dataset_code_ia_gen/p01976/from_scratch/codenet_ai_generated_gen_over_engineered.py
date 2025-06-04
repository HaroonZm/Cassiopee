class FrequencyMap:
    def __init__(self):
        self._freq = {}

    def add(self, key):
        self._freq[key] = self._freq.get(key, 0) + 1

    def remove(self, key):
        if key in self._freq:
            if self._freq[key] == 1:
                del self._freq[key]
            else:
                self._freq[key] -= 1

    def equals(self, other):
        return self._freq == other._freq

    def copy(self):
        new_map = FrequencyMap()
        new_map._freq = self._freq.copy()
        return new_map


class Subsequence:
    def __init__(self, data, start, end):
        # inclusive start, exclusive end
        self._data = data
        self._start = start
        self._end = end

    def as_frequency_map(self):
        freq = FrequencyMap()
        for i in range(self._start, self._end):
            freq.add(self._data[i])
        return freq


class Matcher:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)

    def find_matching_ks(self):
        results = []
        front_freq = FrequencyMap()
        rear_freq = FrequencyMap()
        for i in range(self.length):
            front_freq.add(self.sequence[i])
            rear_freq.add(self.sequence[self.length - 1 - i])
            if front_freq.equals(rear_freq):
                results.append(i + 1)
        return results


class InputReader:
    def __init__(self):
        self.N = 0
        self.sequence = []

    def read(self):
        self.N = int(input())
        self.sequence = list(map(int, input().split()))
        if len(self.sequence) != self.N:
            raise ValueError("Length of sequence does not match N")


class OutputWriter:
    @staticmethod
    def write_matching_ks(ks):
        print(" ".join(map(str, sorted(ks))))
        

def main():
    reader = InputReader()
    reader.read()
    matcher = Matcher(reader.sequence)
    ks = matcher.find_matching_ks()
    OutputWriter.write_matching_ks(ks)


if __name__ == "__main__":
    main()