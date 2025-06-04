class VATPriceCalculator:
    class PricePair:
        def __init__(self, p1: int, p2: int):
            self.p1 = p1
            self.p2 = p2
        
        def total_after_tax(self, rate: int) -> int:
            def after_tax(p: int, r: int) -> int:
                raw = p * (100 + r)
                div, mod = divmod(raw, 100)
                if mod >= 50:
                    div += 1
                return div
            return after_tax(self.p1, rate) + after_tax(self.p2, rate)
        
        def __repr__(self):
            return f"PricePair({self.p1}, {self.p2})"

    class VATChangeScenario:
        def __init__(self, old_rate: int, new_rate: int, old_total: int):
            self.old_rate = old_rate
            self.new_rate = new_rate
            self.old_total = old_total
            self.valid_pairs = []
            self._generate_valid_pairs()
        
        def _generate_valid_pairs(self):
            # We only consider pairs (p, old_total - p) with p in [1, old_total-1]
            # which have the after_tax total at old_rate equal to old_total
            for p1 in range(1, self.old_total):
                p2 = self.old_total - p1
                pair = VATPriceCalculator.PricePair(p1, p2)
                if pair.total_after_tax(self.old_rate) == self.old_total:
                    self.valid_pairs.append(pair)
        
        def maximum_new_total(self) -> int:
            # Among valid pairs, pick max total_after_tax with new_rate
            max_total = 0
            for pair in self.valid_pairs:
                val = pair.total_after_tax(self.new_rate)
                if val > max_total:
                    max_total = val
            return max_total
    
    def __init__(self):
        self.scenarios = []
    
    def add_scenario(self, x: int, y: int, s: int):
        self.scenarios.append(VATPriceCalculator.VATChangeScenario(x, y, s))
    
    def compute_results(self):
        results = []
        for scenario in self.scenarios:
            results.append(scenario.maximum_new_total())
        return results


def main():
    import sys
    calculator = VATPriceCalculator()
    for line in sys.stdin:
        if not line.strip():
            continue
        x, y, s = map(int, line.strip().split())
        if x == 0 and y == 0 and s == 0:
            break
        calculator.add_scenario(x, y, s)
    results = calculator.compute_results()
    for r in results:
        print(r)


if __name__ == "__main__":
    main()