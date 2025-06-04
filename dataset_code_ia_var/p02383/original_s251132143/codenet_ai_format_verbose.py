class Dice:

    def __init__(self, face_labels_list):

        self.face_labels = face_labels_list


    def roll(self, roll_direction):

        if roll_direction == "N":

            self.face_labels[0], self.face_labels[1], self.face_labels[5], self.face_labels[4] = (
                self.face_labels[1], 
                self.face_labels[5], 
                self.face_labels[4], 
                self.face_labels[0]
            )

        elif roll_direction == "S":

            self.face_labels[0], self.face_labels[1], self.face_labels[5], self.face_labels[4] = (
                self.face_labels[4], 
                self.face_labels[0], 
                self.face_labels[1], 
                self.face_labels[5]
            )

        elif roll_direction == "E":

            self.face_labels[0], self.face_labels[2], self.face_labels[5], self.face_labels[3] = (
                self.face_labels[3], 
                self.face_labels[0], 
                self.face_labels[2], 
                self.face_labels[5]
            )

        else:  # Assume "W"

            self.face_labels[0], self.face_labels[2], self.face_labels[5], self.face_labels[3] = (
                self.face_labels[2], 
                self.face_labels[5], 
                self.face_labels[3], 
                self.face_labels[0]
            )


input_face_labels = [int(value) for value in input().split()]

roll_commands_string = input()

dice_instance = Dice(input_face_labels)

for roll_command_char in roll_commands_string:

    dice_instance.roll(roll_command_char)

print(dice_instance.face_labels[0])