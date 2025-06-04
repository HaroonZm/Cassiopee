class Panel:
    def __init__(self, name, points, children):
        self.name = name
        self.x1 = points[0]
        self.y1 = points[1]
        self.x2 = points[2]
        self.y2 = points[3]
        self.children = children
        self.child_cnt = len(children)

    def search(self, x, y):
        # On vérifie si le point (x, y) n'est pas dans le panneau principal
        if x < self.x1 or x > self.x2 or y < self.y1 or y > self.y2:
            return ["OUT", "OF", "MAIN", "PANEL", "1"]
        for child in self.children:
            # On regarde chaque enfant s'il contient le point
            if child.x1 <= x <= child.x2 and child.y1 <= y <= child.y2:
                return child.search(x, y)
        # Sinon, on retourne le nom du panneau et le nombre d'enfants
        return (self.name, self.child_cnt)

def parse_begin_tag(s, pos):
    pos += 1
    name = ""
    # On récupère le nom du panneau
    while s[pos] != ">":
        name += s[pos]
        pos += 1
    pos += 1
    return name, pos

def parse_tag_value(s, pos):
    points = []
    for i in range(4):
        num = ""
        while pos < len(s) and s[pos].isdigit():
            num += s[pos]
            pos += 1
        points.append(int(num))
        pos += 1
    return points, pos - 1

def parse_end_tag(s, pos):
    while s[pos] != ">":
        pos += 1
    pos += 1
    return pos

def parse_tag_structure(s, pos):
    name, pos = parse_begin_tag(s, pos)
    points, pos = parse_tag_value(s, pos)
    children = []
    while True:
        if s[pos+1] == "/":
            break
        child, pos = parse_tag_structure(s, pos)
        children.append(child)
    pos = parse_end_tag(s, pos)
    return Panel(name, points, children), pos

while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    panel, _ = parse_tag_structure(s, 0)
    for i in range(n):
        x, y = map(int, input().split())
        result = panel.search(x, y)
        print(*result)