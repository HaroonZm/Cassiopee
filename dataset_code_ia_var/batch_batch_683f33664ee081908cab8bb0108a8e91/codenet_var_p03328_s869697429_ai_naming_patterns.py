# Cohesive and systematic variable naming
start_value, end_value = map(int, input().split())

difference = end_value - start_value
term_count = difference - 1
sum_terms = ((term_count + 1) * term_count) // 2
result = sum_terms - start_value

print(result)