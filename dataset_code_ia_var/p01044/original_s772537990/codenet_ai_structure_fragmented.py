class Simulator:
    def __init__(self, mp, width, height):
        self.initialize_simulator(mp, width, height)

    def initialize_simulator(self, mp, width, height):
        self.mp = mp
        self.width = width
        self.height = height
        self.vec = self.create_vec()
        self.checked = None
        self.erase_list = None

    def create_vec(self):
        return [
            ((1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (0, 1)),
            ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 1))
        ]

    def rotate(self, x, y):
        if not self.is_valid_rotate_position(x, y):
            return
        vec = self.get_rotation_vec(x)
        last_color = self.get_last_color(x, y, vec)
        self.rotate_colors(x, y, vec, last_color)

    def is_valid_rotate_position(self, x, y):
        return 0 < x < self.width - 1 and 0 < y < self.height - 1

    def get_rotation_vec(self, x):
        return self.vec[x % 2]

    def get_last_color(self, x, y, vec):
        lx, ly = vec[-1]
        return self.mp[y + ly][x + lx]

    def rotate_colors(self, x, y, vec, last_color):
        for i in range(5, 0, -1):
            self.assign_rotation_color(x, y, vec, i)
        self.assign_last_color(x, y, vec, last_color)

    def assign_rotation_color(self, x, y, vec, i):
        ax, ay = vec[i]
        bx, by = vec[i - 1]
        self.mp[y + ay][x + ax] = self.mp[y + by][x + bx]

    def assign_last_color(self, x, y, vec, last_color):
        sx, sy = vec[0]
        self.mp[y + sy][x + sx] = last_color

    def check(self):
        self.initialize_checked_erase()
        for y in range(self.height):
            for x in range(self.width):
                self.check_cell(x, y)

    def initialize_checked_erase(self):
        self.checked = self.create_checked()
        self.erase_list = []

    def create_checked(self):
        return [[False] * self.width for _ in range(self.height)]

    def check_cell(self, x, y):
        if self.already_checked_cell(x, y):
            return
        self.checked[y][x] = True
        if self.cell_is_dot(x, y):
            return
        save = self.create_save(x, y)
        self.perform_search(x, y, save)
        self.add_to_erase_list_if_needed(save)

    def already_checked_cell(self, x, y):
        return self.checked[y][x]

    def cell_is_dot(self, x, y):
        return self.mp[y][x] == "."

    def create_save(self, x, y):
        return [(x, y)]

    def perform_search(self, x, y, save):
        self.search(x, y, save)

    def add_to_erase_list_if_needed(self, save):
        if self.is_minimum_combo(save):
            self.erase_list += save

    def is_minimum_combo(self, save):
        return len(save) >= 3

    def search(self, x, y, save):
        vec = self.get_search_vec(x)
        for dx, dy in vec:
            if not self.is_inside_bounds(x, y, dx, dy):
                continue
            if self.should_skip_cell(x, y, dx, dy):
                continue
            if self.colors_are_equal(x, y, dx, dy):
                self.mark_and_search(x, y, dx, dy, save)

    def get_search_vec(self, x):
        return self.vec[x % 2]

    def is_inside_bounds(self, x, y, dx, dy):
        return 0 <= x + dx < self.width and 0 <= y + dy < self.height

    def should_skip_cell(self, x, y, dx, dy):
        return self.checked[y + dy][x + dx]

    def colors_are_equal(self, x, y, dx, dy):
        return self.mp[y + dy][x + dx] == self.mp[y][x]

    def mark_and_search(self, x, y, dx, dy, save):
        save.append((x + dx, y + dy))
        self.checked[y + dy][x + dx] = True
        self.search(x + dx, y + dy, save)

    def erase(self):
        for x, y in self.erase_list:
            self.erase_single_cell(x, y)

    def erase_single_cell(self, x, y):
        self.mp[y][x] = "."

    def fall(self):
        for y in range(1, self.height):
            self.fall_odd_columns(y)
            self.fall_even_columns(y)

    def fall_odd_columns(self, y):
        for x in range(1, self.width, 2):
            check_vec = self.fall_odd_check_vec(x)
            self.perform_fall(y, x, check_vec)

    def fall_odd_check_vec(self, x):
        if x != self.width - 1:
            return ((-1, -1), (0, -1), (1, -1))
        else:
            return ((-1, -1), (0, -1))

    def fall_even_columns(self, y):
        for x in range(0, self.width, 2):
            check_vec = self.fall_even_check_vec(x)
            self.perform_fall(y, x, check_vec)

    def fall_even_check_vec(self, x):
        if x == 0:
            return ((0, -1), (1, 0))
        elif x == self.width - 1:
            return ((-1, 0), (0, -1))
        else:
            return ((-1, 0), (0, -1), (1, 0))

    def perform_fall(self, y, x, check_vec):
        to_y = y
        while to_y > 0:
            if not self.can_fall(to_y, x, check_vec):
                break
            to_y -= 1
        if to_y != y:
            self.perform_cell_fall(x, y, to_y)

    def can_fall(self, to_y, x, check_vec):
        for dx, dy in check_vec:
            if self.is_blocked(to_y, x, dx, dy):
                return False
        return True

    def is_blocked(self, to_y, x, dx, dy):
        return self.mp[to_y + dy][x + dx] != "."

    def perform_cell_fall(self, x, y, to_y):
        self.mp[to_y][x] = self.mp[y][x]
        self.mp[y][x] = "."

    def run(self):
        LIMIT = 100
        cnt = 0
        while True:
            cnt += 1
            if self.is_limit_over(cnt, LIMIT):
                self.handle_limit_over()
                break
            self.fall()
            self.check()
            if not self.has_erases():
                break
            self.erase()

    def is_limit_over(self, cnt, LIMIT):
        return cnt > LIMIT

    def handle_limit_over(self):
        print("LIMIT_OVER")

    def has_erases(self):
        return bool(self.erase_list)

    def print_mp(self):
        for y in self.y_range_for_print():
            print(self.get_print_row(y))

    def y_range_for_print(self):
        return range(self.height - 1, -1, -1)

    def get_print_row(self, y):
        return "".join(self.mp[y])

def read_hw():
    return map(int, input().split())

def read_map(h):
    return [list(input()) for _ in range(h)][::-1]

def create_simulator(mp, w, h):
    return Simulator(mp, w, h)

def perform_queries(simulator, q):
    for _ in range(q):
        x, y = map(int, input().split())
        simulator.rotate(x, y)
        simulator.run()

def main():
    h, w = read_hw()
    mp = read_map(h)
    simulator = create_simulator(mp, w, h)
    simulator.run()
    q = int(input())
    perform_queries(simulator, q)
    simulator.print_mp()

main()