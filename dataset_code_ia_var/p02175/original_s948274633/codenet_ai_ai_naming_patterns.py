value_current, value_increment_a, value_increment_b = map(int, input().split())
input_count = int(input())
for input_index in range(input_count):
    input_word = input()
    if input_word == "nobiro":
        value_current += value_increment_a
    elif input_word == "tidime":
        value_current += value_increment_b
    elif input_word == "karero":
        value_current = 0
    if value_current < 0:
        value_current = 0
print(value_current)