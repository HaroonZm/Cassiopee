input_string = input()
count_consecutive_r = 0
if "R" in input_string:
    count_consecutive_r = 1
if "RR" in input_string:
    count_consecutive_r = 2
if "RRR" in input_string:
    count_consecutive_r = 3
print(count_consecutive_r)