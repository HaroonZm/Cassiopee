input_string = input()
count_r_three = input_string.count("RRR")
count_r_two = input_string.count("RR")
count_single_r = input_string.count("R")

if count_r_three == 1:
    print(3)
elif count_r_two == 1:
    print(2)
elif count_single_r > 0:
    print(1)
else:
    print(0)