def algorithm():
    """
    Main algorithm loop to process multiple scenarios. For each scenario:
    - Read the target budget.
    - For the next 12 months, read monthly income and outcome.
    - Track the cumulative total balance after each month.
    - Determine the first month (if any) where the running total equals or surpasses the budget.
    - If after 12 months the goal is not met, output 'NA'; otherwise, output the (1-based) month.
    The loop continues until a budget of 0 is entered (which acts as input termination).
    """
    while True:
        # Read the target budget from user input
        budget = int(input())
        if budget == 0:
            # Terminate the loop if budget is zero
            break

        total = 0    # Cumulative balance after each month
        months = 0   # The earliest month (1-based) when total >= budget
        # Read and process financial data for each of the 12 months
        for i in range(12):
            # Read monthly income and outcome
            income, outcome = map(int, input().split())
            # Update the cumulative balance
            total += income - outcome
            # Record the first month when total meets or surpasses the budget
            if total >= budget and months == 0:
                months = i + 1  # Store month number (1-based)

        # Output 'NA' if budget was not achieved in 12 months; otherwise, print the month
        print('NA' if total < budget else months)

def main():
    """
    Entry point function that calls the algorithm.
    """
    algorithm()

if __name__ == '__main__':
    main()