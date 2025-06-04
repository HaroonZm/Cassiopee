input_text = input()
intermediate_placeholder = 'PLACEHOLDER_FRUIT'
input_text = input_text.replace('apple', intermediate_placeholder)
input_text = input_text.replace('peach', 'apple')
input_text = input_text.replace(intermediate_placeholder, 'peach')
print(input_text)