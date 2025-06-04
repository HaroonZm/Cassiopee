from typing import List, Tuple, Dict
from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**7)

class ItemGraph:
    def __init__(self, n_items: int):
        self.n = n_items
        self.edges: Dict[int, List[Tuple[int,int]]] = defaultdict(list)
        # Maintain visited states for DFS cycle detection with ratios
        self.visited = [False]*(self.n+1)
        self.on_stack = [False]*(self.n+1)
        self.value_ratio = [None]*(self.n+1)  # ratio relative to a base in the component
        self.bug_found = False

    def add_rule(self, a: int, b: int, x: int):
        # edge from a to b with ratio x (means 1 a = x b)
        self.edges[a].append((b, x))
        # edge from b to a with ratio 1/x (as integer fraction 1/x)
        # We will store ratio as numerator/denominator to avoid float precision
        # but since problem deals with integer scaling 1 item <-> x other items,
        # ratios can be stored as ints in DFS with fraction comparison
        self.edges[b].append((a, -x))  # -x means reciprocal edge with ratio 1/x

    def dfs(self, node: int, base_num: int, base_den: int) -> None:
        if self.bug_found:
            return
        self.visited[node] = True
        self.on_stack[node] = True
        self.value_ratio[node] = (base_num, base_den)

        for (nxt, ratio) in self.edges[node]:
            if self.bug_found:
                return
            # Compute the ratio of nxt relative to current node
            # If ratio > 0 then 1 node = ratio * nxt => nxt = 1/ratio * node
            # If ratio < 0 then 1 node = 1/abs(ratio) * nxt => nxt = abs(ratio) * node
            # We'll keep ratios as fractions num/den to detect inconsistency cycles

            # Current relation: node = base_num / base_den (base)
            # For edge (node -> nxt):
            #   If ratio >0: 1 node = ratio nxt => nxt = 1/ratio node
            #      nxt = base_num / (base_den * ratio)
            #   If ratio <0: 1 node = 1/abs(ratio) nxt => nxt = abs(ratio) node
            #      nxt = base_num * abs(ratio) / base_den

            if ratio > 0:
                # nxt_num / nxt_den = base_num / (base_den * ratio)
                nxt_num = base_num
                nxt_den = base_den * ratio
            else:
                abs_r = -ratio
                # nxt_num / nxt_den = base_num * abs_r / base_den
                nxt_num = base_num * abs_r
                nxt_den = base_den

            # Reduce fraction by gcd to keep numbers small (optional, but makes equality checks robust)
            def gcd(a: int, b: int) -> int:
                while b:
                    a, b = b, a % b
                return a

            g = gcd(nxt_num, nxt_den)
            nxt_num //= g
            nxt_den //= g

            if not self.visited[nxt]:
                self.dfs(nxt, nxt_num, nxt_den)
                if self.bug_found:
                    return
            else:
                if not self.on_stack[nxt]:
                    # already processed and not on current DFS stack, no cycle
                    continue
                # check ratio consistency:
                # The previously assigned ratio must be equal to the newly computed ratio
                prev_num, prev_den = self.value_ratio[nxt]

                # two fractions prev_num/prev_den and nxt_num/nxt_den must be equal
                if prev_num * nxt_den != prev_den * nxt_num:
                    # inconsistent ratio in a cycle => unlimited increment bug
                    self.bug_found = True
                    return
        self.on_stack[node] = False

class TradingBugDetector:
    def __init__(self, n: int, m: int, rules: List[Tuple[int,int,int]]):
        self.n = n
        self.m = m
        self.rules = rules
        self.graph = ItemGraph(n)

    def build_graph(self) -> None:
        for a, b, x in self.rules:
            self.graph.add_rule(a, b, x)

    def detect_bug(self) -> bool:
        self.build_graph()
        for node in range(1, self.n+1):
            if not self.graph.visited[node]:
                self.graph.dfs(node, 1, 1)
                if self.graph.bug_found:
                    break
        return self.graph.bug_found

class GameTradingChecker:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip().split('\n')
        self.N = 0
        self.M = 0
        self.rules: List[Tuple[int,int,int]] = []

    def parse_input(self):
        self.N, self.M = map(int, self.input_data[0].split())
        for i in range(1, self.M+1):
            a,b,x = map(int, self.input_data[i].split())
            self.rules.append((a,b,x))

    def run_check(self) -> str:
        self.parse_input()
        detector = TradingBugDetector(self.N, self.M, self.rules)
        if detector.detect_bug():
            return "No"
        else:
            return "Yes"

def main():
    # reading from stdin
    raw_data = sys.stdin.read()
    checker = GameTradingChecker(raw_data)
    print(checker.run_check())

if __name__ == "__main__":
    main()