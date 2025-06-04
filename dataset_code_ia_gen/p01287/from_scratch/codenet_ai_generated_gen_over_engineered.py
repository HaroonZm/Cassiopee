class Panel:
    def __init__(self, color: str):
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, Panel):
            return False
        return self.color == other.color

    def __hash__(self):
        return hash(self.color)

    def __repr__(self):
        return f"Panel({self.color})"

class Octahedron:
    # The octahedron has 8 triangular faces arranged such that:
    # 4 form the "top" pyramid and 4 form the "bottom" pyramid, sharing the middle square created by 4 vertices.
    #
    # We model the 8 faces indexed 0 to 7.
    #
    # According to the problem, two octahedra are identical if one can be rotated to form the other.
    # We will encode the rotations as permutations on the face indices.
    #
    # Reference for octahedron rotations: The rotation group of the octahedron is isomorphic to the full symmetric group on 4 vertices of the square face (24 rotations) plus inversions, but since rotations alone suffice, commonly 24 rotations.
    #
    # We only consider rotational symmetries (no reflections), so 24 elements.
    #
    # For simplicity, we will list explicitly the 24 rotations as permutations of the face indices.

    # Indexing faces as:
    # Let's label faces as follows for clarity:
    # - faces 0,1,2,3 form the "top" pyramid faces around the top vertex
    # - faces 4,5,6,7 form the "bottom" pyramid faces around the bottom vertex
    #
    # Their arrangement is symmetric, and rotations permute those indices.

    # We use the numbering consistent with this arrangement:
    #
    #       0
    #     / | \
    #    1--2--3
    #
    # and on the bottom:
    #
    #       4
    #     / | \
    #    5--6--7
    #
    # Actually, faces adjacent and such - but for modeling rotations, the permutations suffice.

    # Define the 24 rotation permutations on faces:
    rotation_permutations = [
        # identity
        [0,1,2,3,4,5,6,7],

        # Rotations around vertical axis (top vertex)
        [0,2,3,1,4,6,7,5],
        [0,3,1,2,4,7,5,6],

        # Rotations exchanging top and bottom pyramids with rotation around horizontal axes
        [4,5,6,7,0,1,2,3],

        [4,6,7,5,0,2,3,1],
        [4,7,5,6,0,3,1,2],

        # Rotations around an axis through edges
        [1,5,2,6,0,4,3,7],
        [1,2,6,3,0,1,7,4],  # This permutation is off, corrected version below

        # We will generate complete 24 rotations for safety:
        # Instead of hardcoding possibly incorrect permutations, we generate the group by combining basic rotations:

    ]

    # To avoid mistakes, let's build the 24 rotations systematically using cube symmetries:
    # Since the Octahedron rotation group is isomorphic to that of the cube, we can generate the group via:
    #
    # We treat top faces as a cycle of 4 (0,1,2,3)
    # And bottom faces as (4,5,6,7)
    # Rotations include:
    # - rotations around axis top-bottom (0,4)
    # - rotations swapping top and bottom faces with flips
    #
    # Here is an algorithm to generate the group:

    @staticmethod
    def generate_rotation_group():
        # Base permutations:
        def rotate_top(f):
            # rotate top faces cycle by +1, bottom similarly
            # 0->1,1->2,2->3,3->0; 4->5,5->6,6->7,7->4
            mapping = [1,2,3,0,5,6,7,4]
            return [f[i] for i in mapping]

        def rotate_bottom(f):
            # rotate bottom faces cycle by +1, top unchanged
            mapping = [0,1,2,3,5,6,7,4]
            return [f[i] for i in mapping]

        def rotate_middle(f):
            # swap top and bottom faces: top face i <-> bottom face i
            mapping = [4,5,6,7,0,1,2,3]
            return [f[i] for i in mapping]

        # generate group by BFS on permutations starting with identity
        from collections import deque

        identity = list(range(8))
        operations = [rotate_top, rotate_middle]

        seen = set()
        queue = deque()
        queue.append(identity)
        seen.add(tuple(identity))

        results = []

        while queue:
            elem = queue.popleft()
            results.append(elem)
            for op in operations:
                new_elem = op(elem)
                if tuple(new_elem) not in seen:
                    seen.add(tuple(new_elem))
                    queue.append(new_elem)

                # Also combine with rotate_top multiple times to get all 4 rotations:
                temp = new_elem
                for _ in range(3):
                    temp = rotate_top(temp)
                    if tuple(temp) not in seen:
                        seen.add(tuple(temp))
                        queue.append(temp)
        return results

    rotations = generate_rotation_group.__func__()

    def __init__(self, panels):
        if len(panels) != 8:
            raise ValueError("Exactly 8 panels required")
        self.panels = panels  # List of Panel objects

    def canonical_form(self):
        # Generate all rotations of the octahedron and get lex smallest string representation
        # of colors under these rotations
        # Return the canonical form string

        color_strings = [p.color for p in self.panels]
        candidates = []
        for perm in self.rotations:
            rotated = [color_strings[i] for i in perm]
            candidates.append(' '.join(rotated))

        return min(candidates)

    def __eq__(self, other):
        if not isinstance(other, Octahedron):
            return False
        return self.canonical_form() == other.canonical_form()

    def __hash__(self):
        return hash(self.canonical_form())

    def __repr__(self):
        return f"Octahedron({self.canonical_form()})"


class OctahedronBuilder:
    def __init__(self, panel_colors):
        # panel_colors is list of 8 strings
        self.panels = [Panel(c) for c in panel_colors]

    def generate_all_distinct_octahedra(self):
        from collections import Counter
        counts = Counter(self.panels)
        # We want number of distinct octahedra that can be formed
        # from exactly these 8 panels (all given panels must be used)

        # Since all 8 panels are the ones provided, the only permutations that produce different octahedra are the permutations of panels.

        # To count distinct octahedra up to rotations, we generate all distinct permutations of the panels and keep those unique modulo rotations
        import itertools

        # Because of repeated colors, using permutations is expensive.
        # We generate unique permutations of panels (multiset permutations).
        # For performance, we'll generate permutations via lexicographic method.

        color_list = [p.color for p in self.panels]
        color_list.sort()

        def multiset_permutations(seq):
            # Generator for unique permutations of seq with duplicates
            # seq sorted list of elements
            def backtrack(path, counter, length):
                if len(path) == length:
                    yield path[:]
                    return
                for x in sorted(counter.keys()):
                    if counter[x] > 0:
                        counter[x] -= 1
                        path.append(x)
                        yield from backtrack(path, counter, length)
                        path.pop()
                        counter[x] += 1

            from collections import Counter
            c = Counter(seq)
            yield from backtrack([], c, len(seq))

        unique_octahedra = set()
        for perm in multiset_permutations(color_list):
            octa = Octahedron([Panel(c) for c in perm])
            unique_octahedra.add(octa)
        return len(unique_octahedra)


class InputParser:
    def __init__(self):
        import sys
        self.lines = sys.stdin.read().strip().split('\n')

    def datasets(self):
        # Each dataset is 8 lines of colors
        # The sample input shows the 8 colors separated by spaces on one line, but problem states 8 lines with one color each.
        # To handle both possibilities:
        # If line has many words, treat as a full dataset of 8 colors in one line.
        # Otherwise, 8 lines each with a single color.

        idx = 0
        n = len(self.lines)
        while idx < n:
            # Try reading 8 lines as 8 colors
            if idx + 8 <= n:
                dataset = self.lines[idx:idx+8]
                # Check if each line is a single color word or multi
                single_colors = all(len(line.split()) == 1 for line in dataset)
                if single_colors:
                    yield dataset
                    idx += 8
                    continue
            # Otherwise, try reading one line with 8 colors
            line = self.lines[idx].strip()
            parts = line.split()
            if len(parts) == 8:
                yield parts
                idx += 1
            else:
                # Input format unknown - break
                break


def main():
    parser = InputParser()
    for dataset in parser.datasets():
        builder = OctahedronBuilder(dataset)
        print(builder.generate_all_distinct_octahedra())

if __name__ == "__main__":
    main()