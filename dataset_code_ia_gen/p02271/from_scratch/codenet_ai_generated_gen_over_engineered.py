class SubsetSumSolverInterface:
    def can_make(self, target: int) -> bool:
        raise NotImplementedError("Subclasses should implement this method")

class RecursiveSubsetSumSolver(SubsetSumSolverInterface):
    def __init__(self, elements):
        self.elements = elements
        self.n = len(elements)
    
    def can_make(self, target: int) -> bool:
        memo = {}
        def solve(p, t):
            if t == 0:
                return True
            if p == self.n or t < 0:
                return False
            if (p, t) in memo:
                return memo[(p, t)]
            # choose p-th element or not
            use_it = solve(p + 1, t - self.elements[p])
            skip_it = solve(p + 1, t)
            memo[(p, t)] = use_it or skip_it
            return memo[(p, t)]
        return solve(0, target)

class QueryProcessor:
    def __init__(self, solver: SubsetSumSolverInterface, queries):
        self.solver = solver
        self.queries = queries
    
    def process_queries(self):
        result = []
        for q in self.queries:
            result.append("yes" if self.solver.can_make(q) else "no")
        return result

class InputParser:
    @staticmethod
    def parse_input():
        n = int(input())
        elements = list(map(int, input().split()))
        q = int(input())
        queries = list(map(int, input().split()))
        return elements, queries

class OutputRenderer:
    @staticmethod
    def render_results(results):
        for res in results:
            print(res)

class ExhaustiveSearchApp:
    def __init__(self):
        self.elements = []
        self.queries = []
        self.solver = None
        self.processor = None
    
    def setup(self):
        self.elements, self.queries = InputParser.parse_input()
        self.solver = RecursiveSubsetSumSolver(self.elements)
        self.processor = QueryProcessor(self.solver, self.queries)
        
    def run(self):
        self.setup()
        results = self.processor.process_queries()
        OutputRenderer.render_results(results)

if __name__ == "__main__":
    app = ExhaustiveSearchApp()
    app.run()