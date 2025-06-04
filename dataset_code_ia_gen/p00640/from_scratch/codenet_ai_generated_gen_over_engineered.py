class Coordinates:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, x: int, y: int) -> bool:
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2


class Button:
    def __init__(self, coords: Coordinates, target_page: str):
        self.coords = coords
        self.target_page = target_page


class Page:
    def __init__(self, name: str):
        self.name = name
        self.buttons = []

    def add_button(self, button: Button):
        self.buttons.append(button)

    def click_at(self, x: int, y: int):
        for button in self.buttons:
            if button.coords.contains(x, y):
                return button.target_page
        return None


class BrowserHistory:
    def __init__(self, initial_page: str):
        self.buffer = [initial_page]
        self.pointer = 0

    def visit(self, page_name: str):
        # Remove forward pages
        if self.pointer < len(self.buffer) - 1:
            self.buffer = self.buffer[: self.pointer + 1]
        self.buffer.append(page_name)
        self.pointer += 1

    def back(self):
        if self.pointer > 0:
            self.pointer -= 1

    def forward(self):
        if self.pointer < len(self.buffer) - 1:
            self.pointer += 1

    def current(self):
        return self.buffer[self.pointer]


class DistortedLoveBrowser:
    def __init__(self, width: int, height: int, pages: dict, start_page: str):
        self.width = width
        self.height = height
        self.pages = pages
        self.history = BrowserHistory(start_page)

    def click(self, x: int, y: int):
        current_page_name = self.history.current()
        current_page = self.pages[current_page_name]
        next_page_name = current_page.click_at(x, y)
        if next_page_name is not None:
            self.history.visit(next_page_name)

    def back(self):
        self.history.back()

    def forward(self):
        self.history.forward()

    def show(self):
        print(self.history.current())


class InputParser:
    def __init__(self):
        pass

    def parse_buttons(self, b: int):
        buttons = []
        for _ in range(b):
            x1, y1, x2, y2, target = input().split()
            x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
            buttons.append(Button(Coordinates(x1, y1, x2, y2), target))
        return buttons

    def parse_pages(self, n: int):
        pages = {}
        for _ in range(n):
            line = input().split()
            name = line[0]
            b = int(line[1])
            page = Page(name)
            buttons = self.parse_buttons(b)
            for button in buttons:
                page.add_button(button)
            pages[name] = page
        return pages

    def parse_operations(self, m: int):
        operations = []
        for _ in range(m):
            line = input().split()
            operations.append(line)
        return operations


def main():
    parser = InputParser()
    while True:
        n = int(input())
        if n == 0:
            break
        W, H = map(int, input().split())
        pages = parser.parse_pages(n)
        start_page = next(iter(pages.keys()))
        distorted_browser = DistortedLoveBrowser(W, H, pages, start_page)
        m = int(input())
        operations = parser.parse_operations(m)

        for op in operations:
            if op[0] == 'click':
                x, y = int(op[1]), int(op[2])
                distorted_browser.click(x, y)
            elif op[0] == 'back':
                distorted_browser.back()
            elif op[0] == 'forward':
                distorted_browser.forward()
            elif op[0] == 'show':
                distorted_browser.show()


if __name__ == "__main__":
    main()