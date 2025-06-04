import copy

def read_and_shuffle():
    """
    Reads lines of input, applies a sequence of shuffles to each line,
    and outputs the result after shuffling.
    Input stops when a single '-' is entered.
    For each line of input:
      - Reads a number representing how many shuffles to perform
      - For each shuffle, reads a number representing the shuffle position
      - Performs the shuffle accordingly and prints the final result
    """
    shuffle_data = []  # Temporary list to hold shuffled data
    copy_data = []     # Working copy of the current data being shuffled

    while True:
        data = input()  # Read a line of input

        if data == "-":
            # If input is '-', break and end input reading
            break

        copy_data.clear()  # Clear the copy_data list for this new input line

        # Copy each character from the input string to the copy_data list
        for i in data:
            copy_data.append(i)

        Number = int(input())  # Number of shuffles to apply

        # Perform shuffles sequentially
        for i in range(Number):
            shuffle_data.clear()  # Prepare shuffle_data for this shuffle
            shuffle_number = int(input())  # Get the shuffle position

            # Move characters from 'shuffle_number' to end to the start
            for j in range(shuffle_number, len(data)):
                shuffle_data.append(copy_data[j])

            # Move characters from start up to 'shuffle_number' to the end
            for j in range(0, shuffle_number):
                shuffle_data.append(copy_data[j])

            # Update copy_data with the shuffled data for the next shuffle
            copy_data.clear()
            for j in shuffle_data:
                copy_data.append(j)

        # After all shuffles, print the result as a string
        for i in shuffle_data:
            print(i, end="")

        print()  # Print a newline for the next result

if __name__ == "__main__":
    read_and_shuffle()