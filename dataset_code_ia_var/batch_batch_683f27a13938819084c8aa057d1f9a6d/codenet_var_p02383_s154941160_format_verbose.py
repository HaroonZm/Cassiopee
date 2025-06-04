class DiceWithNamedFaces:
    def __init__(self, face_numbers_list):
        self.face_numbers_list = face_numbers_list

        self.face_number_mapping = {
            1: face_numbers_list[0],      # Top
            2: face_numbers_list[1],      # Front
            3: face_numbers_list[2],      # Right
            -3: face_numbers_list[3],     # Left
            -2: face_numbers_list[4],     # Back
            -1: face_numbers_list[5]      # Bottom
        }

        self.current_top_face = 1    # Top face code
        self.current_front_face = 2  # Front face code
        self.current_right_face = 3  # Right face code

    def roll_dice(self, direction_character):
        if direction_character == 'N':
            self.current_top_face, self.current_front_face = self.current_front_face, -self.current_top_face
        elif direction_character == 'S':
            self.current_top_face, self.current_front_face = -self.current_front_face, self.current_top_face
        elif direction_character == 'E':
            self.current_top_face, self.current_right_face = -self.current_right_face, self.current_top_face
        elif direction_character == 'W':
            self.current_top_face, self.current_right_face = self.current_right_face, -self.current_top_face

    def print_top_face_number(self):
        top_number = self.face_number_mapping[self.current_top_face]
        print(top_number)

if __name__ == "__main__":
    input_face_numbers = list(map(int, input().split()))
    dice_instance = DiceWithNamedFaces(input_face_numbers)

    movement_command_string = input()

    for single_direction in movement_command_string:
        dice_instance.roll_dice(single_direction)

    dice_instance.print_top_face_number()