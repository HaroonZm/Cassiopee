class Panel:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.children = []

    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

def parse_panel(s, start=0):
    # Parse a panel starting at s[start]
    # Return (panel, next_pos)
    pos = start
    assert s[pos] == '<'
    pos += 1
    # read tag name
    name = ''
    while s[pos] != '>':
        name += s[pos]
        pos += 1
    pos += 1  # skip '>'

    # read coordinates x1,y1,x2,y2
    coords = ''
    while s[pos] in '0123456789,':
        coords += s[pos]
        pos += 1
    x1,y1,x2,y2 = map(int, coords.split(','))

    panel = Panel(name, x1, y1, x2, y2)

    # parse children if any
    while True:
        if s[pos:pos+2] == '</':
            # end tag
            pos += 2
            end_name = ''
            while s[pos] != '>':
                end_name += s[pos]
                pos += 1
            pos += 1  # skip '>'
            assert end_name == name
            break
        elif s[pos] == '<':
            child, pos = parse_panel(s, pos)
            panel.children.append(child)
        else:
            # should not happen
            pos += 1
    return panel, pos

def find_top_panel(panel, x, y):
    if not panel.contains(x,y):
        return None
    # among children, find panel that contains point
    for child in panel.children:
        r = find_top_panel(child, x, y)
        if r is not None:
            return r
    # no child contains point, return self
    return panel

while True:
    n = input()
    if n == '':
        break
    n = int(n)
    if n == 0:
        break
    tag_structure = input()

    root, _ = parse_panel(tag_structure)

    points = []
    for _ in range(n):
        x,y = map(int, input().split())
        points.append((x,y))

    for (x,y) in points:
        panel = find_top_panel(root, x, y)
        if panel is None:
            print("OUT OF MAIN PANEL 1")
        else:
            print(panel.name, len(panel.children))