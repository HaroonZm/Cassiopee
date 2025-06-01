class Panel(object):
    def __init__(self, name, depth, child, x1, y1, x2, y2):
        self.name = name
        self.depth = depth
        self.child = child
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def touch(self, x, y, depth):
        return self._touch_check_depth(depth) and self._touch_check_coords(x, y) and self or None

    def _touch_check_depth(self, depth):
        return depth < self.depth

    def _touch_check_coords(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def __repr__(self):
        return self._repr_name() + " " + self._repr_child()

    def _repr_name(self):
        return self.name

    def _repr_child(self):
        return str(self.child)

def solve():
    import re

    def input_int():
        return int(input())

    def input_str():
        return input()

    def input_ints():
        return map(int, input().split())

    def read_N():
        return input_int()

    def read_S():
        return input_str()

    def create_panel_out_of_main_panel():
        return Panel("OUT OF MAIN PANEL", 0, 1, 0, 0, 10000, 10000)

    def rec_parse_panels(s, depth):
        child = 0
        while s:
            child = increment_child(child)
            tag_name = extract_tag_name(s)
            result = match_panel_pattern(s, tag_name)
            children_count = rec_parse_panels(extract_inner_content(result), depth + 1)
            panel = build_panel_from_match(tag_name, depth, children_count, result)
            add_panel(panel)
            s = extract_remaining_string(s, result)
        return child

    def increment_child(child):
        return child + 1

    def extract_tag_name(s):
        return re.match(r"<([^>]+)>", s).group(1)

    def match_panel_pattern(s, tag_name):
        pattern = r"<%s>(\d+),(\d+),(\d+),(\d+)(.*?)</%s>" % (tag_name, tag_name)
        return re.match(pattern, s)

    def extract_inner_content(result):
        return result.group(5)

    def build_panel_from_match(tag_name, depth, child, result):
        coords = tuple(map(int, result.groups()[:4]))
        return Panel(tag_name, depth, child, *coords)

    def add_panel(panel):
        panels.append(panel)

    def extract_remaining_string(s, result):
        return s[result.span()[1]:]

    panels = []
    while True:
        N = read_N()
        if N == 0:
            break
        S = read_S()
        panels.clear()
        panel_root = create_panel_out_of_main_panel()
        panels.append(panel_root)
        rec_parse_panels(S, 1)
        for _ in range(N):
            x, y = input_ints()
            result_panel = find_touching_panel(x, y)
            print(result_panel)

    def find_touching_panel(x, y):
        current = panels[0]
        for panel in panels[1:]:
            touched = panel.touch(x, y, current.depth)
            if touched is not None:
                current = touched
        return current

if __name__ == "__main__":
    solve()