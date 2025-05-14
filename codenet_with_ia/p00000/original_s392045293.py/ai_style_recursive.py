def print_multiplication_table(n=0):
    if n >= 81:
        return
    i, j = n // 9 + 1, n % 9 + 1
    print(f"{i}x{j}={i*j}")
    print_multiplication_table(n + 1)

print_multiplication_table()