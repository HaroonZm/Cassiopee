class AmidaLadder:
    class VerticalStick:
        def __init__(self, index, score):
            self.index = index
            self.score = score

        def __repr__(self):
            return f"VerticalStick(index={self.index}, score={self.score})"

    class HorizontalBar:
        def __init__(self, index, left_stick_index, height):
            self.index = index
            self.left_stick_index = left_stick_index
            self.height = height

        def __repr__(self):
            return f"HorizontalBar(index={self.index}, left_stick_index={self.left_stick_index}, height={self.height})"

    class LadderState:
        def __init__(self, n, m, h, k, vertical_scores, horizontal_bars):
            self.n = n
            self.m = m
            self.h = h
            self.k = k
            self.vertical_sticks = [AmidaLadder.VerticalStick(i+1, vertical_scores[i]) for i in range(n)]
            self.horizontal_bars = horizontal_bars
            # Represent each level as a mapping of stick connections to establish the current paths
            self.levels = [[] for _ in range(h+1)] # levels from 0 (top) to h (bottom)

            for bar in horizontal_bars:
                self.levels[bar.height].append(bar.left_stick_index)

            # Each level has a set of horizontal bars connecting sticks i and i+1 at that height
            # bars do not share endpoints, so no conflicting connections exist at the same height

        def _simulate_paths(self, removed_bar_index=None):
            # Simulate the amida ladder, potentially with one horizontal bar removed
            # Initially sticks are in positions [1..n]
            # At each height from top to h, the horizontal bars swap the positions of the connected sticks

            sticks = list(range(1, self.n+1))  # positions left to right, sticks identified by original index

            # Create a mapping from (height) to list of bars (except the removed one)
            bars_by_height = [[] for _ in range(self.h+1)]
            for bar in self.horizontal_bars:
                if removed_bar_index is not None and bar.index == removed_bar_index:
                    continue
                bars_by_height[bar.height].append(bar.left_stick_index)

            # For each height, process bars to swap sticks
            for height in range(1, self.h):
                # Bars at this height connect sticks i and i+1. We swap their positions.
                swaps = bars_by_height[height]
                # To avoid double swapping, process swaps in ascending order of left_stick_index
                swaps.sort()
                # We'll build a new stick order by applying swaps in order
                pos_to_stick = sticks
                # Apply swaps: for each left_stick_index i, swap pos i-1 and i (0-based)
                # Note: left_stick_index starts from 1, so position in list is left_stick_index-1
                for left in swaps:
                    left_pos = left -1
                    right_pos = left_pos +1
                    # swap sticks at left_pos and right_pos
                    pos_to_stick[left_pos], pos_to_stick[right_pos] = pos_to_stick[right_pos], pos_to_stick[left_pos]
                sticks = pos_to_stick

            # Now sticks[i] tells which original vertical stick is at position i+1 at bottom
            # The score is the sum of scores of sticks at positions 1 to k (the contiguous k sticks starting at 1)
            # Because J君 chooses vertical sticks 1..k (leftmost k)
            # But because of swaps, positions correspond to possibly different sticks

            # We need sum of the scores of the sticks that ended up at positions 1..k:
            selected_sticks = sticks[:self.k]  # the sticks at positions 1..k
            total_score = sum(self.vertical_sticks[s-1].score for s in selected_sticks)
            return total_score

        def find_min_score(self):
            # Check without removing any bar first
            min_score = self._simulate_paths(removed_bar_index=None)
            # Then try removing each horizontal bar in turn to find the minimal achievable score
            for bar in self.horizontal_bars:
                score = self._simulate_paths(removed_bar_index=bar.index)
                if score < min_score:
                    min_score = score
            return min_score


class InputOutputHandler:
    def __init__(self):
        self.datasets = []

    def read_input(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            n, m, h, k = map(int, lines[idx].split())
            idx += 1
            if n == 0 and m == 0 and h == 0 and k == 0:
                break
            vertical_scores = []
            for _ in range(n):
                vertical_scores.append(int(lines[idx]))
                idx += 1
            horizontal_bars = []
            for i in range(m):
                a_i, b_i = map(int, lines[idx].split())
                idx += 1
                horizontal_bars.append(AmidaLadder.HorizontalBar(i+1, a_i, b_i))
            self.datasets.append((n,m,h,k, vertical_scores, horizontal_bars))

    def process_all(self):
        results = []
        for (n,m,h,k, vertical_scores, horizontal_bars) in self.datasets:
            ladder = AmidaLadder.LadderState(n,m,h,k,vertical_scores,horizontal_bars)
            min_score = ladder.find_min_score()
            results.append(min_score)
        return results

    def output_results(self, results):
        for res in results:
            print(res)


def main():
    ioh = InputOutputHandler()
    ioh.read_input()
    results = ioh.process_all()
    ioh.output_results(results)


if __name__ == "__main__":
    main()