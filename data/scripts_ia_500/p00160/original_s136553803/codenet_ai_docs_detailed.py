def calculate_shipping_costs():
    """
    This function continuously processes multiple sets of package data.
    For each set, it reads an integer 'n' representing the number of packages.
    Then, for each package, it reads four integers: x, y, h, w, representing dimensions and weight.
    It calculates the total shipping cost based on combined dimensions and weight using specified rules.
    The process repeats until 'n' is zero, at which point the function terminates.
    """
    while True:
        # Initialize the total shipping cost for the current set of packages
        total_cost = 0
        # Read the number of packages in the current set
        n = int(input())
        # If n is zero, no more packages to process; exit the loop
        if n == 0:
            break
        # Loop through each package to process its dimensions and weight
        for _ in range(n):
            # Read package dimensions (x, y, h) and weight (w)
            x, y, h, w = map(int, input().split())
            # Calculate the sum of the three dimensions
            dimension_sum = x + y + h
            # Determine shipping cost based on dimension sum and weight criteria
            if dimension_sum <= 60 and w <= 2:
                total_cost += 600
            elif dimension_sum <= 80 and w <= 5:
                total_cost += 800
            elif dimension_sum <= 100 and w <= 10:
                total_cost += 1000
            elif dimension_sum <= 120 and w <= 15:
                total_cost += 1200
            elif dimension_sum <= 140 and w <= 20:
                total_cost += 1400
            elif dimension_sum <= 160 and w <= 25:
                total_cost += 1600
            # Packages not meeting any condition do not add to the total cost
        # After processing all packages in the current set, print the total shipping cost
        print(total_cost)

# Call the function to execute the shipping cost calculation process
calculate_shipping_costs()