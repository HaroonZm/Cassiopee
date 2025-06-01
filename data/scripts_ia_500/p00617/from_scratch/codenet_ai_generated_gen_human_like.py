import sys

sys.setrecursionlimit(10000)

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

def parse_panel(s, pos=0):
    # parse opening tag <name>
    if s[pos] != '<':
        raise ValueError("Expected '<' at pos {}".format(pos))
    end_tag_pos = s.find('>', pos)
    if end_tag_pos == -1:
        raise ValueError("Expected '>' for start tag")

    tag_name = s[pos+1:end_tag_pos]
    pos = end_tag_pos + 1

    # parse tag values: 4 integers separated by commas
    vals_end = pos
    while vals_end < len(s) and (s[vals_end].isdigit() or s[vals_end]==',' or s[vals_end]=='-'):
        vals_end += 1
    vals_str = s[pos:vals_end]
    pos = vals_end

    vals = vals_str.split(',')
    if len(vals)!=4:
        raise ValueError("Expected 4 integers for tag values")
    x1, y1, x2, y2 = map(int, vals)
    panel = Panel(tag_name, x1, y1, x2, y2)

    # parse children panels if any
    while True:
        if pos >= len(s):
            raise ValueError("Unexpected end of string while parsing children")

        if s[pos] == '<':
            if pos+1 < len(s) and s[pos+1] == '/':  # end tag
                break
            # parse child panel recursively
            child, pos = parse_panel(s, pos)
            panel.children.append(child)
        else:
            # unexpected character
            raise ValueError("Unexpected character '{}' at pos {}".format(s[pos], pos))

    # parse end tag
    if not s.startswith('</'+tag_name+'>', pos):
        raise ValueError("End tag does not match start tag '{}' at pos {}".format(tag_name, pos))
    pos += len('</'+tag_name+'>')

    return panel, pos

def find_panel(panel, x, y):
    if not panel.contains(x, y):
        return None
    # check children in order, the last child found that contains point is topmost
    # but since siblings don't overlap, we can do linear search
    for child in panel.children:
        if child.contains(x,y):
            # deeper found panel
            res = find_panel(child, x, y)
            if res is not None:
                return res
            else:
                return child
    # no children contains it, so panel itself is topmost here
    return panel

def main():
    input = sys.stdin.read().strip().split('\n')
    idx=0
    while True:
        if idx>=len(input):
            break
        n = int(input[idx])
        idx+=1
        if n==0:
            break
        tag_str = input[idx]
        idx+=1
        points=[]
        for _ in range(n):
            x,y = map(int,input[idx].split())
            points.append((x,y))
            idx+=1
        # parse panel structure
        root, pos = parse_panel(tag_str,0)
        # find main panel
        if root.name != "main":
            print("OUT OF MAIN PANEL 1")
            continue

        for (x,y) in points:
            p= find_panel(root,x,y)
            if p is None:
                # not inside main
                print("OUT OF MAIN PANEL 1")
            else:
                # print panel name and number of children
                print(p.name, len(p.children))

if __name__ == "__main__":
    main()