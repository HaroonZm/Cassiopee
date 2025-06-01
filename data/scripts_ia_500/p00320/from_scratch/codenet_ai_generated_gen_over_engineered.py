class Rectangle:
    def __init__(self, h: int, w: int):
        self.h, self.w = sorted((h, w))  # normaliser pour comparaison ordonnée

    def __eq__(self, other):
        return (self.h, self.w) == (other.h, other.w)

    def __hash__(self):
        return hash((self.h, self.w))

    def __repr__(self):
        return f"Rectangle({self.h}, {self.w})"


class PaperSet:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def normalized_rectangles(self):
        return sorted(self.rectangles, key=lambda r: (r.h, r.w))


class CuboidValidator:
    def __init__(self, paper_set: PaperSet):
        self.paper_set = paper_set

    def can_form_cuboid(self) -> bool:
        rects = self.paper_set.normalized_rectangles()
        if len(rects) != 6:
            return False
        # Compter la fréquence de chaque rectangle
        freq = {}
        for r in rects:
            freq[r] = freq.get(r, 0) + 1
        # Pour un cuboïde, il doit y avoir exactement 3 dimensions (a,b,c)
        # Les 6 faces sont 2 fois chaque paire (a,b), (b,c), (c,a)

        # Les rectangles doivent être groupés en 3 groupes de 2

        # Vérifier qu'il y a exactement 3 types de rectangles
        if len(freq) != 3:
            return False
        # Chacun apparaissant exactement 2 fois
        if any(count != 2 for count in freq.values()):
            return False

        rect_list = list(freq.keys())
        # Chercher si on peut attribuer a,b,c pour que 
        # rect_list == [(a,b),(b,c),(a,c)] avec a<=b<=c

        # Extraire toutes les longueurs distinctes dans une set
        lengths = set()
        for r in rect_list:
            lengths.add(r.h)
            lengths.add(r.w)
        if len(lengths) != 3:
            # soit cube (reste compatible), soit non
            # cas cube : si tous 3 rects sont equal and all sides equal
            if len(lengths) == 1:
                # tout égal -> cube
                return True
            return False
        sides = sorted(lengths)
        a, b, c = sides

        expected_rects = {Rectangle(a, b), Rectangle(b, c), Rectangle(a, c)}
        return set(rect_list) == expected_rects


class CuboidBuilder:
    def __init__(self, input_data):
        self.input_data = input_data

    def build_paper_set(self) -> PaperSet:
        rectangles = []
        for line in self.input_data:
            h, w = map(int, line.strip().split())
            rectangles.append(Rectangle(h, w))
        return PaperSet(rectangles)


def main():
    import sys
    lines = [sys.stdin.readline() for _ in range(6)]
    builder = CuboidBuilder(lines)
    paper_set = builder.build_paper_set()
    validator = CuboidValidator(paper_set)
    if validator.can_form_cuboid():
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()