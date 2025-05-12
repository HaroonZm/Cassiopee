class Dice:
    def __init__(self, numbers):
        self.numbers = numbers
        self.number_dict = {1:numbers[0], 2:numbers[1], 3:numbers[2], -3:numbers[3], -2:numbers[4], -1: numbers[5]}
        self.top = 1
        self.front = 2
        self.right = 3

    def move(self, direction):
        if direction == 'N':
            self.top, self.front = self.front, -self.top
        elif direction == 'S':
            self.top, self.front = -self.front, self.top
        elif direction == 'E':
            self.top, self.right = -self.right, self.top
        else:
            self.top, self.right = self.right, -self.top

    def show_number(self):
        print(self.number_dict[self.top])

dice = Dice(list(map(int, input().split())))
move_cmd = input()
for char in move_cmd:
    dice.move(char)
dice.show_number()