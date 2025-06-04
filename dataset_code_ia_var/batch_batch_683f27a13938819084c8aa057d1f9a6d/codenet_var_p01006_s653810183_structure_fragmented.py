def get_constant_N():
    return 1000

def get_neighbors_A():
    return ["B", "D"]

def get_neighbors_B():
    return ["A", "C", "E"]

def get_neighbors_C():
    return ["B", "F"]

def get_neighbors_D():
    return ["A", "E", "G"]

def get_neighbors_E():
    return ["B", "D", "F", "H"]

def get_neighbors_F():
    return ["C", "E", "I"]

def get_neighbors_G():
    return ["D", "H"]

def get_neighbors_H():
    return ["E", "G", "I"]

def get_neighbors_I():
    return ["F", "H"]

def get_neighbors_dict():
    neighbors = {}
    neighbors["A"] = get_neighbors_A()
    neighbors["B"] = get_neighbors_B()
    neighbors["C"] = get_neighbors_C()
    neighbors["D"] = get_neighbors_D()
    neighbors["E"] = get_neighbors_E()
    neighbors["F"] = get_neighbors_F()
    neighbors["G"] = get_neighbors_G()
    neighbors["H"] = get_neighbors_H()
    neighbors["I"] = get_neighbors_I()
    return neighbors

def is_length_one(string):
    return len(string) == 1

def get_char_at(string, i):
    return string[i]

def get_next_char(string, i):
    return string[i+1]

def get_all_indices(string):
    return range(len(string) - 1)

def string_len(string):
    return len(string)

def check_single_step(char_from, char_to, neighbors_dict):
    if char_from in neighbors_dict:
        return char_to in neighbors_dict[char_from]
    return False

def check_step_at_index(string, i, neighbors_dict):
    char_from = get_char_at(string, i)
    char_to = get_next_char(string, i)
    return check_single_step(char_from, char_to, neighbors_dict)

def check_all_steps(string, neighbors_dict):
    for i in get_all_indices(string):
        if not check_step_at_index(string, i, neighbors_dict):
            return False
    return True

def check(string, neighbors_dict=None):
    if neighbors_dict is None:
        neighbors_dict = get_neighbors_dict()
    if is_length_one(string):
        return True
    return check_all_steps(string, neighbors_dict)

def input_str():
    return str(input())

def print_str(s):
    print(s)

def process_input_once(neighbors_dict):
    s = input_str()
    if check(s, neighbors_dict):
        print_str(s)

def main_loop():
    N = get_constant_N()
    neighbors_dict = get_neighbors_dict()
    for _ in range(N):
        process_input_once(neighbors_dict)

main_loop()