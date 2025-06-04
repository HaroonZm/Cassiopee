class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.diag_square = width * width + height * height
    def __lt__(self, other):
        return (self.diag_square < other.diag_square) or ((self.diag_square == other.diag_square) and (self.height < other.height))
    def __gt__(self, other):
        return (self.diag_square > other.diag_square) or ((self.diag_square == other.diag_square) and (self.height > other.height))

rectangle_list = []
for height_candidate in range(1, 151):
    for width_candidate in range(height_candidate + 1, 151):
        rectangle_list.append(Rectangle(height_candidate, width_candidate))
rectangle_list = sorted(rectangle_list)

while True:
    input_height, input_width = map(int, input().split())
    if (input_height, input_width) == (0, 0):
        break
    current_rectangle = Rectangle(input_height, input_width)
    for rect in rectangle_list:
        if current_rectangle < rect:
            print(f"{rect.height} {rect.width}")
            break