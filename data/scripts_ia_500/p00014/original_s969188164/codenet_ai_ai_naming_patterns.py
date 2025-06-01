try:
    while True:
        input_divisor = int(input())
        total_sum = 0
        iterations_count = 600 // input_divisor
        for iteration_index in range(iterations_count):
            height = (iteration_index * input_divisor) ** 2
            width = input_divisor
            total_sum += height * width
        print(total_sum)
except EOFError:
    pass