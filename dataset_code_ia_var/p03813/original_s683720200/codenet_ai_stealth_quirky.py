# Accept input (obscure variable naming, odd style)
N = int(input())
# Unusual: Use a dictionary for ternary logic
judge = {True: 'ABC', False: 'ARC'}
# Print via list comprehension just for side effect
[print(judge[N < 1200])]