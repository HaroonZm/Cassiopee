def main():
    """
    Main function to process several test cases for AOJ 2824: Coastline problem.
    For each case, reads the parameters and heights, and outputs the calculated coastline length.
    """
    while True:
        # Parse the parameters: T (number of positions), D (width of coastline), L (minimum height)
        T, D, L = map(int, input().split())
        if T == 0:
            # If T is zero, this signals the end of input; exit the loop
            break

        # List to keep track of positions (indices) that have heights at least 'L'
        qualifying_indices = []
        for i in range(T):
            x = int(input())
            # Store the position index if the height is at least L
            if x >= L:
                qualifying_indices.append(i)

        # Adjust T to be the maximal index (last position index)
        max_index = T - 1
        total_coastline = 0  # To accumulate the final answer (coastline length)

        # Loop to process consecutive qualifying positions, adding their coastline contributions
        for i in range(1, len(qualifying_indices)):
            # x is the standard width D, but we ensure it doesn't go past the last index
            x = D
            if max_index - qualifying_indices[i-1] < D:
                # If not enough space remains up to the last index, limit x accordingly
                x = max_index - qualifying_indices[i-1]
            # Add the minimum between the gap and the allowed width
            if qualifying_indices[i] - qualifying_indices[i-1] < x:
                total_coastline += qualifying_indices[i] - qualifying_indices[i-1]
            else:
                total_coastline += x

        # After processing all qualifying pairs, add the width for the final qualifying position if needed
        if qualifying_indices:
            # If the last segment stretches past the last position, only go up to the last index (not beyond)
            if qualifying_indices[-1] + D > max_index:
                total_coastline += max_index - qualifying_indices[-1]
            else:
                total_coastline += D

        # Print the computed coastline length for this test case
        print(total_coastline)

if __name__ == "__main__":
    main()