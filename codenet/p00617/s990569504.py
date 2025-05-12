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
        if depth < self.depth and self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return self
        else:
            return None

    def __repr__(self):
        return f"{self.name} {self.child}"

def solve():
    import re
    while True:
        N = int(input())
        if N == 0:
            break

        S = input()
        panels = [Panel("OUT OF MAIN PANEL", 0, 1, 0, 0, 10000, 10000)]

        def rec(s, depth):
            child = 0
            while s:
                child += 1
                tag_name = re.match(r"<([^>]+)>", s).group(1)
                result = re.match(r"<%s>(\d+),(\d+),(\d+),(\d+)(.*?)</%s>" % (tag_name, tag_name), s)
                panels.append(Panel(tag_name, depth, rec(result.group(5), depth + 1), *(map(int, result.groups()[:4]))))
                s = s[result.span()[1]:]
            return child

        rec(S, 1)

        for _ in [0]*N:
            x, y = map(int, input().split())
            result = panels[0]
            for panel in panels[1:]:
                result = panel.touch(x, y, result.depth) or result
            print(result)

if __name__ == "__main__":
    solve()