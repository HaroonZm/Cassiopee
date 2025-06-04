user_input = input()
count_o = user_input.count('o')
max_length = 15
required_count = 8
possible_count = count_o + max_length - len(user_input)
result = 'YES' if possible_count >= required_count else 'NO'
print(result)