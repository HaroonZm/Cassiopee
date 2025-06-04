user_input_string = input()

characters_at_even_indices = user_input_string[::2]
characters_at_odd_indices = user_input_string[1::2]

contains_L_at_even_indices = "L" in characters_at_even_indices
contains_R_at_odd_indices = "R" in characters_at_odd_indices

if contains_L_at_even_indices or contains_R_at_odd_indices:
    print("No")
else:
    print("Yes")