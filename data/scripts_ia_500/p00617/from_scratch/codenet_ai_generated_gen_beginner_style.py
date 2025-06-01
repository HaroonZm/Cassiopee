class Panel:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.children = []

    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

def parse_panel(s, start=0):
    # s[start] should be '<'
    assert s[start] == '<'
    i = start+1
    while s[i] != '>':
        i += 1
    name = s[start+1:i]
    # read tag value after >
    j = i+1
    tagvalue_end = j
    # read until next '<'
    while s[tagvalue_end] != '<':
        tagvalue_end += 1
    coord_str = s[j:tagvalue_end]
    coords = coord_str.split(',')
    panel = Panel(name, coords[0], coords[1], coords[2], coords[3])
    pos = tagvalue_end
    # read children if any
    while True:
        if s[pos:pos+2] == '</':
            # end tag
            # check end tag name
            pos2 = pos+2
            while s[pos2] != '>':
                pos2 += 1
            end_name = s[pos+2:pos2]
            assert end_name == name
            return panel, pos2+1
        elif s[pos] == '<':
            child_panel, newpos = parse_panel(s, pos)
            panel.children.append(child_panel)
            pos = newpos
        else:
            # unexpected character
            pos += 1

def find_panel(panel, x, y):
    # check children first (topmost)
    for child in panel.children:
        if child.contains(x, y):
            res = find_panel(child, x, y)
            if res is not None:
                return res
    if panel.contains(x, y):
        return panel
    return None

while True:
    n = input()
    if not n.isdigit():
        continue
    n = int(n)
    if n == 0:
        break
    tag_line = input().strip()
    root_panel, _ = parse_panel(tag_line, 0)
    points = []
    for _ in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))
    for x, y in points:
        p = find_panel(root_panel, x, y)
        if p is None:
            print("OUT OF MAIN PANEL 1")
        else:
            print(p.name, len(p.children))