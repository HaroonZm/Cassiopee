class Panel:
    def __init__(self, name, depth, child, x1, y1, x2, y2):
        self.name = name
        self.depth = depth
        self.child = child
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def touch(self, x, y, depth):
        if depth < self.depth and self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return self
        else:
            return None

    def __repr__(self):
        return self.name + " " + str(self.child)

def solve():
    import re
    while True:
        N = int(input())
        if N == 0:
            break

        S = input()
        panels = []
        panels.append(Panel("OUT OF MAIN PANEL", 0, 1, 0, 0, 10000, 10000))

        def parse_panels(s, depth):
            child = 0
            pos = 0
            while pos < len(s):
                tag_start = s.find('<', pos)
                if tag_start == -1:
                    break
                tag_end = s.find('>', tag_start)
                if tag_end == -1:
                    break
                tag_name = s[tag_start+1:tag_end]
                close_tag = "</" + tag_name + ">"
                close_tag_pos = s.find(close_tag, tag_end)
                if close_tag_pos == -1:
                    break
                inside = s[tag_end+1:close_tag_pos]
                parts = inside.split('>', 1)
                nums_str = parts[0]
                nums = nums_str.strip().split(',')
                if len(nums) >= 4:
                    x1, y1, x2, y2 = map(int, nums[:4])
                    rest = ''
                    if len(parts) > 1:
                        rest = parts[1]
                    child_num = parse_panels(rest, depth+1)
                    child += 1
                    panels.append(Panel(tag_name, depth, child_num, x1, y1, x2, y2))
                pos = close_tag_pos + len(close_tag)
            return child

        parse_panels(S, 1)

        for i in range(N):
            line = input()
            x, y = map(int, line.split())
            result = panels[0]
            for panel in panels[1:]:
                touched = panel.touch(x, y, result.depth)
                if touched:
                    result = touched
            print(result)

if __name__ == "__main__":
    solve()