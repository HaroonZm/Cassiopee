from abc import ABC, abstractmethod
from typing import Optional, Tuple, Iterator

class MeatPurchaseProblem:
    def __init__(self, 
                 min_quantity: int,   # q1 in 100g units
                 budget: int,         # b
                 price_aizu: int,     # c1 per 100g
                 price_normal: int,   # c2 per 100g
                 limit_aizu: int      # q2 max per person (100g units)
                 ):
        self.min_quantity = min_quantity
        self.budget = budget
        self.price_aizu = price_aizu
        self.price_normal = price_normal
        self.limit_aizu = limit_aizu

class SolutionStrategy(ABC):
    @abstractmethod
    def solve(self, problem: MeatPurchaseProblem) -> Optional[Tuple[int,int]]:
        pass

class SophisticatedMeatPurchaseSolver(SolutionStrategy):
    def solve(self, problem: MeatPurchaseProblem) -> Optional[Tuple[int,int]]:
        # Constraints:
        # 1) total grams >= q1 (min_quantity)
        # 2) buy Aizu chicken at least 1 (mandatory)
        # 3) Aizu chicken <= q2 (limit_aizu)
        # 4) budget b is max for total purchase = c1 * aizu + c2 * normal
        # 5) maximize aizu chicken quantity (<= limit)
        # 6) maximize normal chicken quantity with leftover budget after buying aizu
        
        q1 = problem.min_quantity
        b = problem.budget
        c1 = problem.price_aizu
        c2 = problem.price_normal
        q2 = problem.limit_aizu
        
        # Try all feasible aizu chicken quantities from q2 down to 1, to maximize aizu chicken
        # For each, try to maximize normal chicken quantity given leftover budget and total must >= q1
        
        # We pre-optimize by scanning from maximal aizu down to minimal (1)
        
        best_answer = None
        
        # Since q1, q2 <= 1,000,000 and prices up to 1,000,000
        # brute force over q2 (buyable aizu max) is acceptable here (max 1 million, but input constraints say per problem max input 1,000,000, but test cases ~ 50 sets so ok)
        # We can do optimization: we can break early when total quantity is below q1 anyway.
        
        for aizu_qty in range(min(q2, b // c1), 0, -1):
            cost_aizu = aizu_qty * c1
            if cost_aizu > b:
                continue  # Can't afford this much aizu
            
            leftover_budget = b - cost_aizu
            
            # At least total quantity q1, so normal_qty >= q1 - aizu_qty (if positive)
            normal_min = max(0, q1 - aizu_qty)
            
            # Maximum normal quantity we can buy with leftover_budget:
            normal_max = leftover_budget // c2 if c2 > 0 else 0
            
            if normal_max < normal_min:
                # Can't fulfill quantity lower bound with this aizu_qty
                continue
            
            # Among all possible normal quantities from normal_min to normal_max, choose normal_max (maximize normal chicken)
            normal_qty = normal_max
            
            # We have aizu_qty, normal_qty as candidate
            # Verify total quantity >= q1 and budget ok (should be ok)
            total_qty = aizu_qty + normal_qty
            total_cost = aizu_qty * c1 + normal_qty * c2
            
            if total_qty >= q1 and total_cost <= b:
                best_answer = (aizu_qty, normal_qty)
                break  # Since scanning from max aizu down, first found is optimal
        
        return best_answer

class InputParser:
    def __init__(self, source: Iterator[str]):
        self.source = source
    
    def parse(self) -> Iterator[MeatPurchaseProblem]:
        for line in self.source:
            line = line.strip()
            if line == '0':
                break
            if not line:
                continue
            parts = line.split()
            if len(parts) != 5:
                continue
            q1, b, c1, c2, q2 = map(int, parts)
            yield MeatPurchaseProblem(q1, b, c1, c2, q2)

class OutputFormatter:
    @staticmethod
    def format(solution: Optional[Tuple[int,int]]) -> str:
        if solution is None:
            return "NA"
        return f"{solution[0]} {solution[1]}"

class MeatPurchaseApplication:
    def __init__(self, parser: InputParser, solver: SolutionStrategy, formatter: OutputFormatter):
        self.parser = parser
        self.solver = solver
        self.formatter = formatter
    
    def run(self):
        for problem in self.parser.parse():
            solution = self.solver.solve(problem)
            print(self.formatter.format(solution))

if __name__ == "__main__":
    import sys
    app = MeatPurchaseApplication(
        parser=InputParser(iter(sys.stdin.readline, '')),
        solver=SophisticatedMeatPurchaseSolver(),
        formatter=OutputFormatter()
    )
    app.run()