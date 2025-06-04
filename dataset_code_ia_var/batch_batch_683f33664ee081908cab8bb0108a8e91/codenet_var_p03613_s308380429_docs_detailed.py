def main():
    """
    Main function that reads user input, processes a list of integers,
    generates a new list by adding and subtracting 1 to each element,
    counts the frequency of all numbers in the new list,
    and prints the highest frequency.
    """
    # Read a string input (likely indicating the number of elements, but not used)
    n = input()
    
    # Read the next input line, split it into parts, convert each part to int,
    # and build the list 'a'
    a = [int(x) for x in input().split()]

    # Create a new list 'num' which contains:
    # - All elements of 'a'
    # - Each element of 'a' incremented by 1
    # - Each element of 'a' decremented by 1
    num = a + [i + 1 for i in a] + [i - 1 for i in a]

    # Import Counter from the collections module for counting unique elements
    from collections import Counter

    # Count the occurrences of all numbers in the 'num' list
    c = Counter(num)

    # Get the most common element and print its frequency
    # c.most_common(1) returns a list of (element, frequency) tuples,
    # so we access frequency with [0][1]
    print(c.most_common(1)[0][1])

if __name__ == "__main__":
    main()