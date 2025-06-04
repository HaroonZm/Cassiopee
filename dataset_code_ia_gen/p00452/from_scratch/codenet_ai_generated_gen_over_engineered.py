class DartScoreOptimizer:
    class ScoreParts:
        def __init__(self, scores):
            self._scores = scores
        
        def __iter__(self):
            return iter(self._scores)
        
        def __len__(self):
            return len(self._scores)
    
    class ScoreLimit:
        def __init__(self, limit):
            self.limit = limit
    
    class MaxDarts:
        def __init__(self, max_darts):
            self.count = max_darts
    
    class Result:
        def __init__(self, max_score):
            self.max_score = max_score
        
        def __str__(self):
            return str(self.max_score)
    
    class DartThrowSimulation:
        def __init__(self, parts, limit, max_darts):
            self.parts = parts
            self.limit = limit
            self.max_darts = max_darts
        
        def compute(self):
            # dp[number_of_throws][score] = possible or not
            # To avoid memory explosion, we use set of achievable sums per throw count
            achievable_scores = [set() for _ in range(self.max_darts.count + 1)]
            achievable_scores[0].add(0)
            for score in self.parts:
                for throws in range(self.max_darts.count - 1, -1, -1):
                    current_scores = achievable_scores[throws]
                    next_scores = achievable_scores[throws + 1]
                    for s in current_scores:
                        new_score = s + score
                        if new_score <= self.limit.limit:
                            next_scores.add(new_score)
            
            max_reachable = 0
            for throws in range(self.max_darts.count + 1):
                local_max = max(achievable_scores[throws]) if achievable_scores[throws] else 0
                if local_max > max_reachable:
                    max_reachable = local_max
            return DartScoreOptimizer.Result(max_reachable)
    
    def __init__(self):
        self.datasets = []
    
    def add_dataset(self, n, m, points):
        self.datasets.append((self.ScoreParts(points), self.ScoreLimit(m), self.MaxDarts(4)))
    
    def run(self):
        results = []
        for parts, limit, max_darts in self.datasets:
            simulation = self.DartThrowSimulation(parts, limit, max_darts)
            results.append(simulation.compute())
        return results


def main():
    import sys
    optimizer = DartScoreOptimizer()
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        n, m = map(int, line.strip().split())
        if n == 0 and m == 0:
            break
        points = []
        while len(points) < n:
            line = sys.stdin.readline()
            if not line:
                return
            points.extend(map(int, line.strip().split()))
        points = points[:n]
        optimizer.add_dataset(n, m, points)
    results = optimizer.run()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()