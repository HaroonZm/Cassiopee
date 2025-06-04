import sys
sys.setrecursionlimit(10**7)

class FormulaNode:
    def evaluate_cost(self, desired):
        raise NotImplementedError()

class LeafNode(FormulaNode):
    def __init__(self, char):
        self.char = char
    def evaluate_cost(self, desired):
        # Returns (cost to fix value=0, cost to fix value=1)
        if self.char == '0':
            # Already 0
            return (0 if desired == 0 else float('inf'))
        elif self.char == '1':
            # Already 1
            return (float('inf') if desired == 0 else 0)
        else:
            # '?': cost 0 if we don't pay and both 0 AND 1 lead to same evaluation
            # but here we decide cost depending on desired:
            # cost 0 if fixing to desired is not necessary (no change in result)
            # cost 1 if fixing needed
            # We'll set cost 1 if forced to choose:
            # But to simplify, for leaf '?', cost 0 if desired achievable w/o fixing is only possible if both 0 and 1 lead to desired.
            # Here both 0 and 1 can equal desired with pay 1 (to fix one choice).
            # Actually if we fix it we pay 1, but if doesn't change result no payment.
            return (0 if desired == 0 else float('inf')) if False else float('inf')
        # In practice we never call for leaf '?' directly but in combined nodes.

class UnknownNode(FormulaNode):
    def __init__(self):
        pass
    def evaluate_cost(self, desired):
        # If we decide to fix this '?':
        # fixing to 0 cost 1, fixing to 1 cost 1
        # without fixing, both possible, so if fixing can be avoided cost 0
        # But without context we return both costs:
        # We'll never use this isolated.
        return (1 if desired == 0 else float('inf'),
                1 if desired == 1 else float('inf'))

class QuestionNode(FormulaNode):
    def __init__(self):
        pass
    def evaluate_cost(self, desired):
        # we must pay 1 if fixing '?', so cost 1 for either desired=0 or 1
        # But if both setting '?' to 0 or 1 yield same evaluation, cost 0 (do not fix)
        # But this depends on parent formula evaluation, so handled at higher level nodes.
        return (1 if desired == 0 else float('inf'),
                1 if desired == 1 else float('inf'))

class ConstNode(FormulaNode):
    def __init__(self, val):
        self.val = val
    def evaluate_cost(self, desired):
        if self.val == desired:
            return 0
        else:
            return float('inf')

class UnknownLeaf(FormulaNode):
    def evaluate_cost(self, desired):
        # Deciding with surrounding nodes
        return 1

class BinaryOpNode(FormulaNode):
    def __init__(self,left,right,op):
        self.left = left
        self.right = right
        self.op = op # '&' or '|'

    def evaluate_cost(self, desired):
        # Returns minimal cost to guarantee value == desired for this subtree
        # Considering short circuit logic
        # We compute dp arrays for all possibilities
        # For each desired value (0 or 1), compute minimal cost

        # We'll iterate on possible left and right evaluations and costs
        # For left and right: value 0 or 1
        # cost to force left value and right value

        costs = {}
        # precompute cost for all desired values for left and right
        left_costs = [self.left.evaluate_cost(d) for d in (0,1)]
        right_costs = [self.right.evaluate_cost(d) for d in (0,1)]

        res_cost = float('inf')

        if self.op == '&':  # a&b:
            # Eval for desired=1 => left=1 and right=1
            if desired == 1:
                # both must be 1
                cost = left_costs[1] + right_costs[1]
                res_cost = cost
            else:
                # desired 0 => either left=0 or right=0 to get 0
                # because of short circuit, if left=0 then right not evaluated -> only cost left_0
                cost0 = left_costs[0] # short circuit, right not evaluated
                # or left=1 and right=0
                cost1 = left_costs[1] + right_costs[0]
                res_cost = min(cost0, cost1)
        else:  # op == '|'
            if desired == 1:
                # desired 1: left=1 or right=1
                # either left=1 (short circuit), cost = left_costs[1],
                # or left=0 and right=1, cost = left_costs[0] + right_costs[1]
                cost0 = left_costs[1]
                cost1 = left_costs[0] + right_costs[1]
                res_cost = min(cost0, cost1)
            else:
                # desired 0: both left=0 and right=0
                cost = left_costs[0] + right_costs[0]
                res_cost = cost

        return res_cost

class QuestionVariable(FormulaNode):
    # Represents a '?'
    def __init__(self):
        pass

    def evaluate_cost(self, desired):
        # Without fixing:
        # evaluation may be different for 0 or 1
        # With fixing:
        # cost +1 to fix to desired
        # We can fix or not fix:
        # If not fix and both 0 and 1 assignments can affect final value => cost infinity
        # But we do not know effect here, so at leaf level: cost 1 to fix desired, 0 if ignoring?

        # We'll decide cost 1 to fix desired
        # but if ignoring, cost 0 if setting to either 0 or 1 yields same eval, otherwise must fix

        # Here we assume cost 1 to fix
        return 1

class Parser:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.pos = 0

    def parse(self):
        node = self.parse_or()
        return node

    def peek(self):
        if self.pos < self.n:
            return self.s[self.pos]
        return ''

    def consume(self):
        ch = self.peek()
        self.pos += 1
        return ch

    def parse_or(self):
        node = self.parse_and()
        while self.peek() == '|':
            self.consume()
            rhs = self.parse_and()
            node = BinaryOpNode(node,rhs,'|')
        return node

    def parse_and(self):
        node = self.parse_term()
        while self.peek() == '&':
            self.consume()
            rhs = self.parse_term()
            node = BinaryOpNode(node,rhs,'&')
        return node

    def parse_term(self):
        c = self.peek()
        if c == '(':
            self.consume()
            node = self.parse_or()
            if self.peek() == ')':
                self.consume()
            return node
        elif c == '0' or c == '1':
            self.consume()
            return ConstNode(int(c))
        elif c == '?':
            self.consume()
            return QuestionVariable()
        else:
            # Should not occur
            self.consume()
            return ConstNode(0)

class Evaluator:
    def __init__(self, root):
        self.root = root

    def compute(self):
        # We want minimal cost to fix expression to 0 and 1
        cost0 = self._eval(self.root, 0)
        cost1 = self._eval(self.root, 1)
        return cost0, cost1

    def _eval(self, node, desired):
        if isinstance(node, ConstNode):
            return 0 if node.val == desired else float('inf')

        if isinstance(node, QuestionVariable):
            # If we do not fix, then the '?' can be either 0 or 1
            # If changing '?' can change output, cost 1
            # We consider cost 1 to fix to desired
            return 1

        if isinstance(node, BinaryOpNode):
            return node.evaluate_cost(desired)

        # Should not reach here
        return float('inf')

def main():
    s = sys.stdin.readline().strip()
    parser = Parser(s)
    root = parser.parse()

    # Because of short circuit logic, we must implement a DP including the notion of whether the '?' must be forced

    # We will map the formula to a DAG with memoization

    memo = {}

    def dfs(node, desired):
        key = (id(node), desired)
        if key in memo:
            return memo[key]
        if isinstance(node, ConstNode):
            memo[key] = 0 if node.val == desired else float('inf')
            return memo[key]
        if isinstance(node, QuestionVariable):
            # There are two cases:
            # If we fix '?', cost = 1

            # If not fix, result is undetermined, so if desired can be both 0 or 1 by replacing '?', cost=0 else must fix

            # But '?' alone: setting 0 or 1 means result changed between two sides => must fix, cost=1

            memo[key] = 1
            return 1
        if isinstance(node, BinaryOpNode):
            op = node.op
            l = node.left
            r = node.right
            if op == '&':
                if desired == 1:
                    # left=1 and right=1
                    cost = dfs(l,1) + dfs(r,1)
                    memo[key] = cost
                    return cost
                else:
                    # desired=0: left=0 or right=0
                    # due to short circuit:
                    # option1 : left=0 (right not evaluated)
                    c1 = dfs(l,0)
                    # option2: left=1 and right=0
                    c2 = dfs(l,1) + dfs(r,0)
                    cost = min(c1,c2)
                    memo[key] = cost
                    return cost
            else: # op == '|'
                if desired == 1:
                    # desired=1: left=1 or right=1
                    # option1: left=1 (right not evaluated)
                    c1 = dfs(l,1)
                    # option2: left=0 and right=1
                    c2 = dfs(l,0) + dfs(r,1)
                    cost = min(c1,c2)
                    memo[key] = cost
                    return cost
                else:
                    # desired=0: left=0 and right=0
                    cost = dfs(l,0) + dfs(r,0)
                    memo[key] = cost
                    return cost
        # unknown case
        memo[key] = float('inf')
        return float('inf')

    cost0 = dfs(root,0)
    cost1 = dfs(root,1)
    print(cost0, cost1)

if __name__ == "__main__":
    main()