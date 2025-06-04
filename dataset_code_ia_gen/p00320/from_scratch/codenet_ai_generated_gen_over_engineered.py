class Rectangle:
    def __init__(self, h: int, w: int):
        self.h = h
        self.w = w

    def normalized(self):
        return (min(self.h, self.w), max(self.h, self.w))

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.normalized() == other.normalized()

    def __hash__(self):
        return hash(self.normalized())

    def __repr__(self):
        return f"Rectangle{self.normalized()}"


class RectanglesCollection:
    def __init__(self, rectangles):
        if len(rectangles) != 6:
            raise ValueError("Exactly 6 rectangles must be provided")
        self.rectangles = rectangles

    def normalized_counts(self):
        counts = {}
        for rect in self.rectangles:
            norm = rect.normalized()
            counts[norm] = counts.get(norm, 0) + 1
        return counts

    def can_form_cuboid(self):
        counts = self.normalized_counts()
        # There must be exactly 3 unique rectangles, each appearing twice
        if len(counts) != 3:
            return False
        if any(count != 2 for count in counts.values()):
            return False
        # Now the three rectangles represent the three pairs of faces of cuboid
        # The dimensions of the cuboid should be a tuple (a,b,c)
        # Each rectangle is one of (a,b), (b,c), (a,c)
        rects = list(counts.keys())
        # Extract all edge lengths and try to find if such a,b,c exist
        edges = []
        for r in rects:
            edges += r
        edges = set(edges)
        if len(edges) not in {2,3}:
            return False  # Impossible to form cuboid edges

        # For three unique edges a,b,c, their pairs should form rectangles
        # or for cube case when only one edge
        # We try to find a,b,c that satisfy the rectangle set
        # An algorithm:
        # Since we have 3 rectangles: r0,r1,r2
        # We try all permutations of edges assignment:

        from itertools import permutations

        # Try to interpret the three face rectangles as (a,b),(b,c),(a,c)

        for a,b,c in permutations(edges, 3):
            faces = {(min(a,b), max(a,b)), (min(b,c), max(b,c)), (min(a,c), max(a,c))}
            if set(rects) == faces:
                return True

        # Also handle cube case: all rectangles are same (a,a)
        # Then edges = {a}
        if len(edges) == 1:
            e = next(iter(edges))
            if all(r == (e,e) for r in rects):
                return True

        return False


class CuboidValidator:
    def __init__(self):
        pass

    def read_input(self):
        rectangles = []
        import sys
        for _ in range(6):
            h, w = map(int, sys.stdin.readline().strip().split())
            rectangles.append(Rectangle(h,w))
        return RectanglesCollection(rectangles)

    def validate(self):
        rc = self.read_input()
        if rc.can_form_cuboid():
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    validator = CuboidValidator()
    validator.validate()