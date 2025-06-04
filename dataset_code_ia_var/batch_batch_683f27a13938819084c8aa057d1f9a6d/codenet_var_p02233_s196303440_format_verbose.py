def memoize_function(original_function):

    computed_values_cache = {}

    def compute_or_get_from_cache(argument):

        if argument not in computed_values_cache:
            computed_values_cache[argument] = original_function(argument)

        return computed_values_cache[argument]

    return compute_or_get_from_cache


@memoize_function
def calculate_fibonacci_number(fibonacci_index):

    if fibonacci_index == 0:
        return 1

    elif fibonacci_index == 1:
        return 1

    return (
        calculate_fibonacci_number(fibonacci_index - 1)
        + calculate_fibonacci_number(fibonacci_index - 2)
    )


user_input_index = int(input("Enter Fibonacci index: "))

print(calculate_fibonacci_number(user_input_index))