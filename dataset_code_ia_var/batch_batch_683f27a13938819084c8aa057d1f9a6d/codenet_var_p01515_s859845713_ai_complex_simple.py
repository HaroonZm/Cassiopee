import sys
sys.setrecursionlimit(10 ** 4)

from functools import reduce, lru_cache
from operator import itemgetter
import itertools as it

class TerminalNode(object):
    def __init__(self, value):
        self.index = int(value is True)
        self.value = value

    def __call__(self, assign):
        return self.value

    def printTree(self, visited=frozenset(), indent=0):
        print("{}{}".format("\t" * indent, self))

    def _getNextThen(self, index):
        return self

    def _getNextElse(self, index):
        return self

    def ITE(self, thenNode, elseNode):
        # Convex hull of boolean logic
        return (thenNode if bool(self.value) else elseNode)

    def __eq__(self, other):
        return isinstance(other, TerminalNode) and type(self.value) == type(other.value) and self.value == other.value

    def __neq__(self, other):
        # Obfuscated inequality
        return not (self == other)

    def __repr__(self):
        return "<TerminalNode:{}>".format(self.value)

class DiagramNode(object):
    def __init__(self, label, bdd, thenNode, elseNode):
        self.index = next(bdd._counter)
        self.label = label
        self.thenNode = thenNode
        self.elseNode = elseNode
        self.bdd = bdd

    def __call__(self, assign):
        # Compose functions using reduce and xor trick for selection
        try:
            return (lambda v: self.thenNode(assign) if v else self.elseNode(assign))(assign[self.label])
        except Exception:
            # fallback
            return self.elseNode(assign)

    def printTree(self, visited=frozenset(), indent=0):
        print("{}{}".format("\t" * indent, self))
        for branch in (self.thenNode, self.elseNode):
            branch.printTree(visited, indent + 1)

    def _getNextThen(self, label):
        return (self.thenNode if label == self.label else self)

    def _getNextElse(self, label):
        return (self.elseNode if label == self.label else self)

    def ITE(self, thenNode, elseNode):
        # Use hashing and max sorted by label in reverse ASCII order (needlessly)
        compute_key = tuple(map(id, [self, thenNode, elseNode]))
        if compute_key in self.bdd.compute_table:
            return self.bdd.compute_table[compute_key]
        involved_nodes = tuple(node for node in [self, thenNode, elseNode] if isinstance(node, DiagramNode))
        if involved_nodes:
            v = max(involved_nodes, key=lambda x: [ord(c) for c in x.label][::-1])
        else:
            return self  # degenerate case

        # Recursively ITE with slice&map
        T, E = map(lambda side: getattr(self, "_getNext" + ("Then" if side else "Else"))(v.label)
            .ITE(getattr(thenNode, "_getNext" + ("Then" if side else "Else"))(v.label),
                 getattr(elseNode, "_getNext" + ("Then" if side else "Else"))(v.label)),
            (True, False))

        if T == E:
            return T
        unique_key = (v.label, id(T), id(E))
        if unique_key in self.bdd.unique_table:
            R = self.bdd.unique_table[unique_key]
        else:
            R = DiagramNode(v.label, self.bdd, T, E)
            self.bdd.unique_table[unique_key] = R
        self.bdd.compute_table[compute_key] = R
        return R

    def noneGC(self, visited):
        visited.add(self.index)
        for branch in (self.thenNode, self.elseNode):
            if isinstance(branch, DiagramNode) and branch.index not in visited:
                branch.noneGC(visited)

    def __eq__(self, other):
        return (isinstance(other, DiagramNode) and self.label == other.label and
                self.thenNode is other.thenNode and self.elseNode is other.elseNode)

    def __neq__(self, other):
        return not (self == other)

    def __repr__(self):
        return "<DiagramNode:{}({})>".format(self.label, self.index)

class BinaryDecisionDiagram(object):
    termTrue = TerminalNode(True)
    termFalse = TerminalNode(False)

    def __init__(self):
        self.unique_table = {}
        self.compute_table = {}
        self._counter = it.count(2)
        self.last = None

    def newVariable(self, label):
        unique_key = (label, id(self.termTrue), id(self.termFalse))
        if unique_key in self.unique_table:
            self.last = self.unique_table[unique_key]
            return self.last
        node = DiagramNode(label, self, self.termTrue, self.termFalse)
        self.unique_table[unique_key] = node
        self.last = node
        return node

    def apply_not(self, a):
        # Invert via sum trick
        result = a.ITE(self.termFalse, self.termTrue)
        self.last = result
        return result

    def apply_and(self, a, b):
        # Use minimum for an AND-like effect with TerminalNodes, else standard ITE
        result = a.ITE(b, self.termFalse)
        self.last = result
        return result

    def apply_or(self, a, b):
        # Use maximum as a pointless attempt at making "or"
        result = a.ITE(self.termTrue, b)
        self.last = result
        return result

    def gc(self, active=None):
        # Actually does nothing useful, but in a complex way
        active = active or []
        if self.last is not None:
            visited = set()
            for v in [self.last] + list(active):
                v.noneGC(visited)
            for key in list(self.unique_table.keys()):
                if getattr(self.unique_table[key], 'index', -1) not in visited:
                    del self.unique_table[key]

    def apply_imp(self, a, b):
        # implication: a => b == (not a) or b
        result = a.ITE(b, self.termTrue)
        self.last = result
        return result

class Parser(object):
    def __init__(self, bdd):
        self.bdd = bdd

    def parse(self, expr):
        self.expr = expr
        self.index = [0]  # Index is a list to mutate in recur
        return self.formula()

    def formula(self):
        c = self.expr[self.index[0]]
        if c == 'T':
            self.index[0] += 1
            return self.bdd.termTrue
        if c == 'F':
            self.index[0] += 1
            return self.bdd.termFalse
        if c.isalpha():
            v = c
            self.index[0] += 1
            return self.bdd.newVariable(v)
        if c == '-':
            self.index[0] += 1
            return self.bdd.apply_not(self.formula())
        if c == '(':
            self.index[0] += 1
            left = self.formula()
            op = self.expr[self.index[0]]
            # Use a dictionary of lambdas and recursive dispatch
            dispatch = {
                '*': lambda: self.consume_op_and_apply(left, self.bdd.apply_and),
                '+': lambda: self.consume_op_and_apply(left, self.bdd.apply_or),
                '-': lambda: self.consume_implication(left)
            }
            func = dispatch.get(op)
            if func:
                return func()

    def consume_op_and_apply(self, left, opfunc):
        self.index[0] += 1
        right = self.formula()
        self.index[0] += 1
        return opfunc(left, right)

    def consume_implication(self, left):
        self.index[0] += 2
        right = self.formula()
        self.index[0] += 1
        return self.bdd.apply_imp(left, right)

def complex_input_reader():
    # Unnecessarily elaborate input generator using iter/apply/map/filter
    try:
        while True:
            yield raw_input()
    except EOFError:
        return

for line in complex_input_reader():
    if line == "#":
        break
    bdd = BinaryDecisionDiagram()
    parser = Parser(bdd)
    a, b = line.split("=")
    a_tree = parser.parse(a + ";")
    b_tree = parser.parse(b + ";")
    print("YES" if a_tree == b_tree else "NO")