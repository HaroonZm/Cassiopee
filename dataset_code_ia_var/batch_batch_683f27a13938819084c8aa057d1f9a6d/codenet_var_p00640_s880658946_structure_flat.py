class Page:
    def __init__(self, name, buttons):
        self.name = name
        self.buttons = buttons

class Button:
    def __init__(self, line):
        self.x1 = int(line[0])
        self.y1 = int(line[1])
        self.x2 = int(line[2])
        self.y2 = int(line[3])
        self.link = line[4]

while True:
    n = int(input())
    if n == 0:
        break
    input()
    pages = {}
    first_page = None
    for i in range(n):
        name, bi = input().split()
        buttons = []
        for _ in range(int(bi)):
            line = input().split()
            x1 = int(line[0])
            y1 = int(line[1])
            x2 = int(line[2])
            y2 = int(line[3])
            link = line[4]
            button = Button([x1, y1, x2, y2, link])
            buttons.append(button)
        page = Page(name, buttons)
        pages[name] = page
        if i == 0:
            first_page = page
    pointer = 0
    length = 0
    contents = [first_page]
    buffer_pages = pages

    m = int(input())
    for _ in range(m):
        s = input()
        if s == "show":
            print(contents[pointer].name)
        elif s == "back":
            pointer = max(0, pointer - 1)
        elif s == "forward":
            pointer = min(length, pointer + 1)
        else:
            parts = s.split()
            x = int(parts[1])
            y = int(parts[2])
            page = contents[pointer]
            found = False
            for button in page.buttons:
                if button.x1 <= x <= button.x2 and button.y1 <= y <= button.y2:
                    link = button.link
                    contents = contents[:pointer+1]
                    contents.append(buffer_pages[link])
                    pointer += 1
                    length = pointer
                    break