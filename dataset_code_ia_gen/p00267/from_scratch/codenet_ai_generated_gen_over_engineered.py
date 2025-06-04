class MonsterBattleSimulator:
    def __init__(self, own_levels, opponent_levels):
        self.own_levels = sorted(own_levels)
        self.opponent_levels = sorted(opponent_levels)
        self.N = len(own_levels)

    def can_win_with_k(self, k):
        # Determine if there exists a selection of k monsters from own_levels
        # so that no matter how opponent selects k monsters, we can win > k/2 times.
        # Equivalent to checking if we have strictly more than k/2 monsters that can beat
        # opponent's k strongest monsters no matter the order.

        half = k // 2 + 1
        # We try to pick our top k monsters from own_levels
        own_top = self.own_levels[-k:]
        # Opponent can pick any k monsters; worst case opponent picks his k strongest monsters to minimize our wins
        opp_top = self.opponent_levels[-k:]

        # We count how many of our chosen monsters can beat opponent's monsters
        # since both sorted ascending, we want to count for how many indices own_top[i] > opp_top[j].
        # We try a greedy matchup: for each opponent monster from smallest to largest
        # assign the smallest own monster that can beat it
        # We simulate using two pointers to count max wins with fixed own selection and worst opponent selection.

        i = 0  # own_top pointer
        j = 0  # opp_top pointer
        wins = 0
        while i < k and j < k:
            if own_top[i] > opp_top[j]:
                wins += 1
                i += 1
                j += 1
            else:
                i += 1
        return wins >= half


class AbstractInputReader:
    def __init__(self):
        pass

    def read_all_datasets(self):
        datasets = []
        while True:
            n = self.read_int_line()
            if n == 0:
                break
            own_levels = self.read_int_list_line()
            opponent_levels = self.read_int_list_line()
            datasets.append((n, own_levels, opponent_levels))
        return datasets

    def read_int_line(self):
        raise NotImplementedError

    def read_int_list_line(self):
        raise NotImplementedError


class StdInputReader(AbstractInputReader):
    def read_int_line(self):
        while True:
            line = input()
            if line.strip():
                return int(line.strip())

    def read_int_list_line(self):
        while True:
            line = input()
            if line.strip():
                return list(map(int, line.strip().split()))


class AbstractOutput:
    def __init__(self):
        pass

    def write_line(self, line):
        raise NotImplementedError


class StdOutput(AbstractOutput):
    def write_line(self, line):
        print(line)


class BattleSolution:
    def __init__(self, input_reader, output_writer):
        self.input_reader = input_reader
        self.output_writer = output_writer

    def solve(self):
        datasets = self.input_reader.read_all_datasets()
        for n, own_levels, opponent_levels in datasets:
            simulator = MonsterBattleSimulator(own_levels, opponent_levels)
            result = self.find_min_k(simulator, n)
            self.output_writer.write_line(result)

    def find_min_k(self, simulator, n):
        # binary search for minimal k (1 <= k < N) such that simulator.can_win_with_k(k) is True
        left = 1
        right = n - 1
        answer = None
        while left <= right:
            mid = (left + right) // 2
            if simulator.can_win_with_k(mid):
                answer = mid 
                right = mid - 1
            else:
                left = mid + 1
        if answer is None:
            return "NA"
        else:
            return answer


def main():
    input_reader = StdInputReader()
    output_writer = StdOutput()
    solution = BattleSolution(input_reader, output_writer)
    solution.solve()


if __name__ == "__main__":
    main()