user_input = input()
char_dict = {}
for char_index in range(len(user_input)):
    char_dict[user_input[char_index]] = True
if len(user_input) == len(char_dict):
    print("yes")
else:
    print("no")