input_count = int(input())
value_a = 1
value_b = 1
for _ in range(input_count):
    input_a, input_b = map(int, input().split())
    multiplier = max(-(-value_a // input_a), -(-value_b // input_b))
    value_a = input_a * multiplier
    value_b = input_b * multiplier
print(value_a + value_b)