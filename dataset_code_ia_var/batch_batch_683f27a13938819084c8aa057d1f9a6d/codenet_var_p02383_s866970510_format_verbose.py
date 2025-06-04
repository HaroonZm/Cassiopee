class Dice:
    def __init__(self, face_one_value, face_two_value, face_three_value, face_four_value, face_five_value, face_six_value):

        # List containing the values of each face in order: [top, front, right, left, back, bottom]
        self.face_values = [
            face_one_value,
            face_two_value,
            face_three_value,
            face_four_value,
            face_five_value,
            face_six_value
        ]

        # The top face is initially 1 (index in face_values is 0)
        self.current_top_face_index = 1

        # Indices for Up, Down, Left, Right faces (relative positions)
        # These numbers represent the face numbers opposite to each face (for standard dice)
        self.udlr_face_indices = [5, 2, 4, 3]

        # Not used in current logic but kept for compatibility
        self.direction_move_count = 0

    def move_dice(self, direction):

        if direction == "E":
            right_face_index = self.udlr_face_indices[2]
            self.udlr_face_indices = [
                self.udlr_face_indices[0],
                self.udlr_face_indices[1],
                7 - self.current_top_face_index,
                self.current_top_face_index
            ]
            self.current_top_face_index = right_face_index

        if direction == "N":
            down_face_index = self.udlr_face_indices[1]
            self.udlr_face_indices = [
                self.current_top_face_index,
                7 - self.current_top_face_index,
                self.udlr_face_indices[2],
                self.udlr_face_indices[3]
            ]
            self.current_top_face_index = down_face_index

        if direction == "S":
            up_face_index = self.udlr_face_indices[0]
            self.udlr_face_indices = [
                7 - self.current_top_face_index,
                self.current_top_face_index,
                self.udlr_face_indices[2],
                self.udlr_face_indices[3]
            ]
            self.current_top_face_index = up_face_index

        if direction == "W":
            left_face_index = self.udlr_face_indices[3]
            self.udlr_face_indices = [
                self.udlr_face_indices[0],
                self.udlr_face_indices[1],
                self.current_top_face_index,
                7 - self.current_top_face_index
            ]
            self.current_top_face_index = left_face_index

    def get_top_face_value(self):

        return self.face_values[self.current_top_face_index - 1]


dice_face_values = list(map(int, input().split()))
movement_commands = input()
dice_instance = Dice(
    *dice_face_values
)
for movement_direction in movement_commands:
    dice_instance.move_dice(movement_direction)

print(dice_instance.get_top_face_value())