input_count = int(input())
input_values = list(map(int, input().split()))
current_count = 0
adjustment_total = 0
adjustment_decrement = -1
while current_count != input_count:
    adjustment_total -= adjustment_decrement
    adjustment_decrement -= 1
    current_count += 1
print(sum(input_values) - adjustment_total)