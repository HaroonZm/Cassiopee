def generate_multiplication_tables():
    # Create a list representing the numbers from 1 to 9
    nums = range(1, 10)
    
    # Utilize map to apply a lambda that generates each line of the table
    # Use chain from itertools to flatten the nested iteration
    from itertools import chain
    tables = map(lambda i_j: f"{i_j[0]}x{i_j[1]}={i_j[0]*i_j[1]}", chain.from_iterable(((i, j) for j in range(1, 10)) for i in nums))
    
    # Print each formatted string in tables
    for line in tables:
        print(line)

generate_multiplication_tables()