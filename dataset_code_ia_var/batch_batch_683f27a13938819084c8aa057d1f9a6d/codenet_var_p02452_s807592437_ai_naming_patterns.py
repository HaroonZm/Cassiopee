input_stream = open(0)
read_line = input_stream.readline

input_num_a = int(read_line())
set_a = set(map(int, read_line().split()))
input_num_b = int(read_line())
set_b = set(map(int, read_line().split()))

intersection_set = set_a & set_b
is_full_intersection = len(intersection_set) == input_num_b

print(+is_full_intersection)