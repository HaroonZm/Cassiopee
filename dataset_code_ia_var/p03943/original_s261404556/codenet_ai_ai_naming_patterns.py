input_value_1, input_value_2, input_value_3 = map(int, input().split())
if (input_value_1 == input_value_2 + input_value_3 or
    input_value_2 == input_value_3 + input_value_1 or
    input_value_3 == input_value_1 + input_value_2):
    print("Yes")
else:
    print("No")