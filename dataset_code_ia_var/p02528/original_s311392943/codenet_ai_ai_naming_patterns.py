user_input = input()
number_list = map(int, raw_input().split())
number_list = sorted(number_list)
output_string = ""
for number_element in number_list:
    output_string += " " + str(number_element)
print output_string[1:]