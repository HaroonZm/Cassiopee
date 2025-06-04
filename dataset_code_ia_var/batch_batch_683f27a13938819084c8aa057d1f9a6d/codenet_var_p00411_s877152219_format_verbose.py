number_of_items, time_taken, rate_per_unit = list(map(int, input().split()))

result_of_calculation = rate_per_unit * time_taken / number_of_items

print("{:.6f}".format(result_of_calculation))