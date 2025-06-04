from typing import List, Dict, Optional, Iterator, Tuple

class Person:
    def __init__(self, name: str):
        self.name = name
        self.parent: Optional['Person'] = None
        self.children: List['Person'] = []
    def add_child(self, child: 'Person'):
        self.children.append(child)
        child.parent = self
    def is_parent_of(self, other: 'Person') -> bool:
        return other in self.children
    def is_child_of(self, other: 'Person') -> bool:
        return self.parent == other
    def is_sibling_of(self, other: 'Person') -> bool:
        return self.parent is not None and self.parent == other.parent and self != other
    def is_ancestor_of(self, other: 'Person') -> bool:
        current = other.parent
        while current:
            if current == self:
                return True
            current = current.parent
        return False
    def is_descendant_of(self, other: 'Person') -> bool:
        return other.is_ancestor_of(self)

class FamilyTree:
    def __init__(self):
        self.members: Dict[str, Person] = {}
        self.root: Optional[Person] = None
    def add_person(self, name: str, indent: int, indent_stack: List[Tuple[int, Person]]):
        person = Person(name)
        self.members[name] = person
        if indent == 0:
            self.root = person
            indent_stack.clear()
            indent_stack.append((indent, person))
        else:
            # Find parent
            # The parent has indent one less
            while indent_stack and indent_stack[-1][0] >= indent:
                indent_stack.pop()
            if indent_stack:
                parent = indent_stack[-1][1]
                parent.add_child(person)
            indent_stack.append((indent, person))
    def get_person(self, name: str) -> Optional[Person]:
        return self.members.get(name)

class Statement:
    def __init__(self, text: str, tree: FamilyTree):
        # Parse statement of form:
        # X is a child of Y.
        # X is the parent of Y.
        # X is a sibling of Y.
        # X is a descendant of Y.
        # X is an ancestor of Y.
        # Text format guaranteed as described, with no extraneous spaces.
        self.text = text
        self.tree = tree
        self.subject_name = ''
        self.object_name = ''
        self.relationship = ''
        self.parse()
    def parse(self):
        # Split into words. X is the first, Y is last before period
        # Relationship is words in between "is" and "of"
        tokens = self.text.strip('.').split(' ')  # Remove trailing dot
        # Format always "X is (a|the) <relationship> of Y"
        # tokens[0] = X
        # tokens[1] = is
        # tokens[2] = a or the
        # tokens[3] = relationship
        # tokens[4] = of
        # tokens[5] = Y
        self.subject_name = tokens[0]
        self.object_name = tokens[5]
        self.relationship = tokens[3]
    def evaluate(self) -> bool:
        subj = self.tree.get_person(self.subject_name)
        obj = self.tree.get_person(self.object_name)
        if not subj or not obj:
            return False
        rel = self.relationship
        if rel == 'parent':
            return subj.is_parent_of(obj)
        elif rel == 'child':
            return subj.is_child_of(obj)
        elif rel == 'sibling':
            return subj.is_sibling_of(obj)
        elif rel == 'ancestor':
            return subj.is_ancestor_of(obj)
        elif rel == 'descendant':
            return subj.is_descendant_of(obj)
        else:
            # Unknown relation, safe false
            return False

class FamilyTreeSolver:
    def __init__(self):
        self.trees: List[FamilyTree] = []
    def process_dataset(self, n: int, m: int, lines: Iterator[str]) -> List[str]:
        # Read family tree
        tree = FamilyTree()
        indent_stack: List[Tuple[int, Person]] = []
        for _ in range(n):
            line = next(lines)
            indent = 0
            while indent < len(line) and line[indent] == ' ':
                indent += 1
            name = line[indent:]
            # Add person and link parent accordingly
            tree.add_person(name, indent, indent_stack)
        results = []
        for _ in range(m):
            statement_line = next(lines)
            statement = Statement(statement_line, tree)
            results.append("True" if statement.evaluate() else "False")
        return results

def main():
    import sys
    lines = iter(sys.stdin.read().splitlines())
    solver = FamilyTreeSolver()
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break
        if not line.strip():
            continue
        n_m = line.split()
        if len(n_m) != 2:
            continue
        n, m = int(n_m[0]), int(n_m[1])
        if n == 0 and m == 0:
            break
        results = solver.process_dataset(n, m, lines)
        for res in results:
            print(res)
        print()

if __name__ == "__main__":
    main()