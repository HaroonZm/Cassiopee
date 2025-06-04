class Dice:
    def __init__(self, face_labels):
        self.top_face_label = face_labels[0]
        self.front_face_label = face_labels[1]
        self.right_face_label = face_labels[2]
        self.left_face_label = face_labels[3]
        self.rear_face_label = face_labels[4]
        self.bottom_face_label = face_labels[5]

    def roll(self, direction):
        if direction == 'N':
            (self.top_face_label,
             self.front_face_label,
             self.bottom_face_label,
             self.rear_face_label) = (
                self.front_face_label,
                self.bottom_face_label,
                self.rear_face_label,
                self.top_face_label
            )
        elif direction == 'E':
            (self.top_face_label,
             self.left_face_label,
             self.bottom_face_label,
             self.right_face_label) = (
                self.left_face_label,
                self.bottom_face_label,
                self.right_face_label,
                self.top_face_label
            )
        elif direction == 'W':
            (self.top_face_label,
             self.right_face_label,
             self.bottom_face_label,
             self.left_face_label) = (
                self.right_face_label,
                self.bottom_face_label,
                self.left_face_label,
                self.top_face_label
            )
        elif direction == 'S':
            (self.top_face_label,
             self.rear_face_label,
             self.bottom_face_label,
             self.front_face_label) = (
                self.rear_face_label,
                self.bottom_face_label,
                self.front_face_label,
                self.top_face_label
            )

    def print_top_face_label(self):
        print(self.top_face_label)


face_labels_input = list(map(int, input().split()))

roll_directions_list = list(input())

dice_instance = Dice(face_labels_input)

for roll_direction in roll_directions_list:
    dice_instance.roll(roll_direction)

dice_instance.print_top_face_label()