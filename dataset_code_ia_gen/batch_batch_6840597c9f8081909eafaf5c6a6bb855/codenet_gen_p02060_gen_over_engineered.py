class TeaPackage:
    def __init__(self, name: str, price: int, cups: int):
        self.name = name
        self.price = price
        self.cups = cups

    def __repr__(self):
        return f"TeaPackage({self.name}, price={self.price}, cups={self.cups})"


class TeaOrderOptimizer:
    def __init__(self, packages: list[TeaPackage], required_cups: int):
        self.packages = packages
        self.required_cups = required_cups
        self.dp = [float('inf')] * (required_cups + max(p.cups for p in packages) + 1)
        self.dp[0] = 0

    def compute_min_cost(self) -> int:
        max_cups_to_check = self.required_cups + max(p.cups for p in self.packages)
        for i in range(max_cups_to_check):
            if self.dp[i] == float('inf'):
                continue
            for package in self.packages:
                next_cups = i + package.cups
                if next_cups < len(self.dp):
                    new_cost = self.dp[i] + package.price
                    if new_cost < self.dp[next_cups]:
                        self.dp[next_cups] = new_cost
        # Find minimum cost for any amount >= required_cups
        min_cost = min(self.dp[self.required_cups:])
        return min_cost


class TeaContestSolver:
    def __init__(self):
        self.N = 0
        self.packages = []

    def read_input(self):
        self.N = int(input().strip())
        prices = list(map(int, input().strip().split()))
        cups = list(map(int, input().strip().split()))
        package_names = ['A', 'B', 'C', 'D']
        self.packages = [TeaPackage(n, p, c) for n, p, c in zip(package_names, prices, cups)]

    def solve(self):
        optimizer = TeaOrderOptimizer(self.packages, self.N)
        answer = optimizer.compute_min_cost()
        print(answer)


def main():
    solver = TeaContestSolver()
    solver.read_input()
    solver.solve()


if __name__ == "__main__":
    main()