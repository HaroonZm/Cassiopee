input_repeat_count = int(input())
input_letters = list(input())
upper_a_m = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
upper_n_z = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_a_m = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
lower_n_z = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_delta = 0
lower_delta = 0
result_string = ""
for current_letter in input_letters:
    if current_letter in upper_a_m:
        upper_delta += 1
    elif current_letter in upper_n_z:
        upper_delta -= 1
    elif current_letter in lower_a_m:
        lower_delta += 1
    elif current_letter in lower_n_z:
        lower_delta -= 1
total_movement = abs(upper_delta) + abs(lower_delta)
print(total_movement)
if total_movement > 0:
    if upper_delta > 0:
        result_string += "A" * upper_delta
    elif upper_delta < 0:
        result_string += "N" * abs(upper_delta)
    if lower_delta > 0:
        result_string += "a" * lower_delta
    elif lower_delta < 0:
        result_string += "n" * abs(lower_delta)
    print(result_string)