def main():
    import sys
    sys.setrecursionlimit(10000)

    def build_tree(n, lines):
        parents = {}
        depths = []
        names = []
        for line in lines:
            stripped = line.lstrip(' ')
            depth = len(line) - len(stripped)
            names.append(stripped)
            depths.append(depth)

        stack = []
        for i in range(n):
            while stack and depths[stack[-1]] >= depths[i]:
                stack.pop()
            if stack:
                parents[names[i]] = names[stack[-1]]
            else:
                parents[names[i]] = None
            stack.append(i)
        return parents, names

    def is_ancestor(ancestor, descendant, parents):
        # traverse up from descendant
        current = descendant
        while current is not None:
            if current == ancestor:
                return True
            current = parents.get(current)
        return False

    def is_descendant(descendant, ancestor, parents):
        return is_ancestor(ancestor, descendant, parents)

    def is_parent(p, c, parents):
        return parents.get(c) == p

    def is_child(c, p, parents):
        return is_parent(p, c, parents)

    def is_sibling(a, b, parents):
        if a == b:
            return False
        return parents.get(a) is not None and parents.get(a) == parents.get(b)

    for line in sys.stdin:
        line=line.rstrip('\n')
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        family_lines = [sys.stdin.readline().rstrip('\n') for _ in range(n)]
        parents, names = build_tree(n, family_lines)
        for _ in range(m):
            stmt = sys.stdin.readline().rstrip('\n')
            # parse statement
            # format: X is a <relation> of Y.
            parts = stmt.split()
            X = parts[0]
            relation = parts[3]
            Y = parts[-1][:-1]  # remove trailing '.'

            if relation == 'child':
                print("True" if is_child(X, Y, parents) else "False")
            elif relation == 'parent':
                print("True" if is_parent(X, Y, parents) else "False")
            elif relation == 'sibling':
                print("True" if is_sibling(X, Y, parents) else "False")
            elif relation == 'descendant':
                print("True" if is_descendant(X, Y, parents) else "False")
            elif relation == 'ancestor':
                print("True" if is_ancestor(X, Y, parents) else "False")
        print()

if __name__ == "__main__":
    main()