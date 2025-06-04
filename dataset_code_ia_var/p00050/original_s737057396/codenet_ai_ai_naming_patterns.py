user_input = input()

step1_intermediate = user_input.replace('apple', '___temp___')
step2_intermediate = step1_intermediate.replace('peach', 'apple')
final_output = step2_intermediate.replace('___temp___', 'peach')

print(final_output)