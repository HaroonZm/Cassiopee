class FrequencyCounter:
    def __init__(self, data):
        self._data = data
        self._frequencies = {}
    
    def count(self):
        for item in self._data:
            self._frequencies[item] = self._frequencies.get(item, 0) + 1
        return self._frequencies

class ModeFinder:
    def __init__(self, frequency_dict):
        self._frequency_dict = frequency_dict

    def find_modes(self):
        if not self._frequency_dict:
            return []
        max_freq = max(self._frequency_dict.values())
        modes = [k for k, v in self._frequency_dict.items() if v == max_freq]
        modes.sort()
        return modes

class InputReader:
    def __init__(self):
        self._raw_data = []
    
    def read_input(self):
        try:
            while True:
                line = input()
                if line.strip() == "":
                    break
                value = int(line.strip())
                if 1 <= value <= 100:
                    self._raw_data.append(value)
                # could raise or ignore out of bound values; here ignore silently
        except EOFError:
            pass
        return self._raw_data

class ModeValueProgram:
    def __init__(self):
        self.reader = InputReader()
        self.counter = None
        self.mode_finder = None
        self.data = []

    def run(self):
        self.data = self.reader.read_input()
        self.counter = FrequencyCounter(self.data)
        frequencies = self.counter.count()
        self.mode_finder = ModeFinder(frequencies)
        modes = self.mode_finder.find_modes()
        for mode in modes:
            print(mode)

if __name__ == "__main__":
    program = ModeValueProgram()
    program.run()