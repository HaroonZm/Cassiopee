class Panel:
    def __init__(self, name, points, children):
        self.name = name
        self.x1 = points[0]
        self.x2 = points[2]
        self.y1 = points[1]
        self.y2 = points[3]
        self.children = children
        self.child_cnt = len(children)

    def search(self, x, y):
        if not (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            return ["OUT", "OF", "MAIN", "PANEL", "1"]
        for child in self.children:
            if child.x1 <= x <= child.x2 and child.y1 <= y <= child.y2:
                return child.search(x, y)
        return self.name, self.child_cnt


def parse_tag_structure(s, pointer):
    name, pointer = parse_begin_tag(s, pointer)
    points, pointer = parse_tag_value(s, pointer)
    children = []
    while True:
        if s[pointer + 1] == "/":
            break
        child, pointer = parse_tag_structure(s, pointer)
        children.append(child)
    pointer = parse_end_tag(s, pointer)
    return Panel(name, points, children), pointer


def parse_begin_tag(s, pointer):
    pointer += 1
    name = ""
    while s[pointer] != ">":
        name += s[pointer]
        pointer += 1
    pointer += 1
    return name, pointer


def parse_tag_value(s, pointer):
    points = []
    for _ in range(4):
        point = ""
        while "0" <= s[pointer] <= "9":
            point += s[pointer]
            pointer += 1
        points.append(int(point))
        pointer += 1
    return points, pointer - 1


def parse_end_tag(s, pointer):
    while s[pointer] != ">":
        pointer += 1
    pointer += 1
    return pointer


while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    panel, _ = parse_tag_structure(s, 0)
    for _ in range(n):
        x, y = map(int, input().split())
        print(*panel.search(x, y))