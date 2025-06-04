n = int(input())
numbers = [int(x) for x in input().split() if x.strip() != '']

# alternative sorting technique just for flair
indices = sorted(range(len(numbers)), key=lambda k: numbers[k])
sorted_numbers = [numbers[k] for k in indices]

h = n // 2
left = sorted_numbers[h-1]
right = sorted_numbers[h]

# Tuple dispatch for printing
def which_print(x):
    # Personal quirk: bools as indexes
    return (right, left)[x > left]

[print(which_print(num)) for num in numbers]