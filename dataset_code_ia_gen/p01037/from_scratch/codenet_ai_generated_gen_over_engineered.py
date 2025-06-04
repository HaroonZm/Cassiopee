class CircularWall:
    def __init__(self, length):
        self.length = length
        self._painted = [False] * length
    
    class Painter:
        def __init__(self, start, length, wall):
            self.start = start % wall.length
            self.length = length
            self.wall = wall
        
        def paint(self):
            n = self.wall.length
            end = (self.start + self.length) % n
            if self.length == n:
                # Paint the whole wall
                for i in range(n):
                    self.wall._painted[i] = True
            elif self.start < end:
                # Non wrap-around interval
                for i in range(self.start, end):
                    self.wall._painted[i] = True
            else:
                # Wrap-around interval
                for i in range(self.start, n):
                    self.wall._painted[i] = True
                for i in range(0, end):
                    self.wall._painted[i] = True
    
    def paint_intervals(self, intervals):
        painters = []
        for a, l in intervals:
            painter = CircularWall.Painter(a, l, self)
            painters.append(painter)
            painter.paint()
        return self._find_painted_intervals()
    
    def _find_painted_intervals(self):
        intervals = []
        n = self.length
        visited = [False] * n
        for i in range(n):
            if self._painted[i] and not visited[i]:
                length = 0
                idx = i
                while self._painted[idx] and not visited[idx]:
                    visited[idx] = True
                    length += 1
                    idx = (idx +1) % n
                    if idx == i:
                        break
                intervals.append(length)
        intervals.sort(reverse=True)
        return intervals

class IntervalAggregator:
    def __init__(self, intervals):
        self.intervals = intervals
    
    def aggregate(self):
        count_map = {}
        for length in self.intervals:
            count_map[length] = count_map.get(length, 0) +1
        result = sorted(count_map.items(), key=lambda x: -x[0])
        return result

class WhiteWallSolver:
    def __init__(self):
        self.wall = None
        self.intervals = []
    
    def input_data(self):
        import sys
        data = sys.stdin.read().strip().split()
        N, M = int(data[0]), int(data[1])
        self.wall = CircularWall(N)
        self.intervals = [(int(data[i*2 + 2]), int(data[i*2 +3])) for i in range(M)]
    
    def solve(self):
        painted_intervals = self.wall.paint_intervals(self.intervals)
        aggregator = IntervalAggregator(painted_intervals)
        aggregated = aggregator.aggregate()
        return aggregated
    
    def output_result(self, aggregated):
        for length, count in aggregated:
            print(length, count)

def main():
    solver = WhiteWallSolver()
    solver.input_data()
    result = solver.solve()
    solver.output_result(result)

if __name__ == "__main__":
    main()