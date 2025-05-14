def print_multiplication_table(i=1, j=1):
    if i > 9:
        return
    if j > 9:
        print_multiplication_table(i + 1, 1)
    else:
        print(f"{i}x{j}={i*j}")
        print_multiplication_table(i, j + 1)

print_multiplication_table()