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
        if not self.is_inside(x, y):
            return self.outside_result()
        return self.search_children_or_self(x, y)

    def is_inside(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def outside_result(self):
        return ["OUT", "OF", "MAIN", "PANEL", "1"]

    def search_children_or_self(self, x, y):
        for child in self.children:
            if child.is_inside(x, y):
                return child.search(x, y)
        return self.name, self.child_cnt

def parse_tag_structure(s, pointer):
    name, pointer = parse_begin_tag(s, pointer)
    points, pointer = parse_tag_value(s, pointer)
    children, pointer = parse_children_list(s, pointer)
    pointer = parse_end_tag(s, pointer)
    return Panel(name, points, children), pointer

def parse_begin_tag(s, pointer):
    pointer = skip_char(s, pointer, '<')
    name, pointer = collect_name_until(s, pointer, '>')
    pointer += 1
    return name, pointer

def skip_char(s, pointer, char):
    while pointer < len(s) and s[pointer] == char:
        pointer += 1
    return pointer

def collect_name_until(s, pointer, stop_char):
    name = ""
    while pointer < len(s) and s[pointer] != stop_char:
        name += s[pointer]
        pointer += 1
    return name, pointer

def parse_tag_value(s, pointer):
    points = []
    for _ in range(4):
        pointer = consume_non_digits(s, pointer)
        point_str, pointer = collect_digits(s, pointer)
        points.append(int(point_str))
        pointer = consume_non_digits(s, pointer)
    pointer -= 1
    return points, pointer

def consume_non_digits(s, pointer):
    while pointer < len(s) and not s[pointer].isdigit():
        pointer += 1
    return pointer

def collect_digits(s, pointer):
    digits = ""
    while pointer < len(s) and s[pointer].isdigit():
        digits += s[pointer]
        pointer += 1
    return digits, pointer

def parse_children_list(s, pointer):
    children = []
    while next_tag_is_begin(s, pointer):
        child, pointer = parse_tag_structure(s, pointer)
        children.append(child)
    return children, pointer

def next_tag_is_begin(s, pointer):
    pos = pointer
    while pos < len(s):
        if s[pos] == '<':
            if pos + 1 < len(s) and s[pos + 1] == '/':
                return False
            else:
                return True
        pos += 1
    return False

def parse_end_tag(s, pointer):
    while pointer < len(s) and s[pointer] != '>':
        pointer += 1
    pointer += 1
    return pointer

def read_input_number():
    return int(input())

def read_input_string():
    return input()

def read_point_coordinates():
    x, y = map(int, input().split())
    return x, y

def main_loop():
    while True:
        n = read_input_number()
        if n == 0:
            break
        s = read_input_string()
        panel, _ = parse_tag_structure(s, 0)
        for _ in range(n):
            x, y = read_point_coordinates()
            result = panel.search(x, y)
            print(*result)

main_loop()