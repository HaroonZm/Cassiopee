class MoveStrategy:
    def next_move(self, remaining: int) -> int:
        raise NotImplementedError


class IchiroStrategy(MoveStrategy):
    def next_move(self, remaining: int) -> int:
        # Ichiro always takes (remaining - 1) % 5 pieces
        count = (remaining - 1) % 5
        return count if count != 0 else 1


class JiroStrategy(MoveStrategy):
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0
        self.length = len(sequence)

    def next_move(self, remaining: int) -> int:
        move = self.sequence[self.index % self.length]
        self.index += 1
        return min(move, remaining)


class Player:
    def __init__(self, name, strategy: MoveStrategy):
        self.name = name
        self.strategy = strategy

    def move(self, remaining: int) -> int:
        return self.strategy.next_move(remaining)


class PebbleGame:
    INITIAL_COUNT = 32

    def __init__(self, jiro_seq):
        self.remaining = PebbleGame.INITIAL_COUNT
        self.jiro = Player("Jiro", JiroStrategy(jiro_seq))
        self.ichiro = Player("Ichiro", IchiroStrategy())
        self.turn_order = [self.ichiro, self.jiro]
        self.turn_index = 0

    def play_turn(self):
        current_player = self.turn_order[self.turn_index]
        move_count = current_player.move(self.remaining)
        self.remaining -= move_count
        self.turn_index = (self.turn_index + 1) % 2
        return self.remaining

    def play_all(self):
        results = []
        while self.remaining > 0:
            results.append(self.play_turn())
        return results


class InputParser:
    def __init__(self):
        pass

    def parse(self, lines):
        datasets = []
        idx = 0
        while idx < len(lines):
            n_line = lines[idx].strip()
            idx += 1
            if n_line == '0':
                break
            n = int(n_line)
            seq_line = lines[idx].strip()
            idx += 1
            seq = list(map(int, seq_line.split()))
            datasets.append(seq)
        return datasets


class OutputFormatter:
    def __init__(self):
        pass

    def format_output(self, results_list):
        output_lines = []
        for results in results_list:
            for val in results:
                output_lines.append(str(val))
        return "\n".join(output_lines)


def main():
    import sys

    lines = [line for line in sys.stdin if line.strip() != '']
    parser = InputParser()
    datasets = parser.parse(lines)
    all_results = []
    for seq in datasets:
        game = PebbleGame(seq)
        results = game.play_all()
        all_results.append(results)
    formatter = OutputFormatter()
    print(formatter.format_output(all_results))


if __name__ == "__main__":
    main()