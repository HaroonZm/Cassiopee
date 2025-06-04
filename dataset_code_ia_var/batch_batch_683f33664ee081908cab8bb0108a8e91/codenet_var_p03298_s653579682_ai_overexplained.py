def main():
    # Read an integer input from the user which represents the half-length of string s (since s will be length 2*n)
    n = int(input())  # 'input()' reads a line from input, 'int()' converts it to an integer

    # Read another input string from the user which should be of length 2 * n
    s = input()  # This line reads the string input

    # Create two empty dictionaries d1 and d2, which will be used to store tuple keys mapping to integer counters
    # In Python, dictionaries are collections that store key-value pairs for fast lookup and counting
    d1 = dict()
    d2 = dict()

    # Create two lists named temp1 and temp2, each of length n, initialized with None values.
    # These will be used for temporary storage during string permutation constructions
    temp1 = [None] * n  # [None] * n makes a list where every element is None
    temp2 = [None] * n

    # Loop over all possible combinations ('ii') for selecting n positions out of 2*n (using bitmasks)
    # range(2 ** n) generates all bitmasks of length n (from 0 to 2^n - 1)
    for ii in range(2 ** n):
        # Convert integer ii to its binary string representation, padded with leading zeroes to length n
        # 'bin(ii)' converts integer to binary string prefixed with '0b', [2:] removes that prefix
        # concatenation with "0"*n pads with enough zeroes to ensure correct length, [-n:] slices the last n chars
        i = ("0" * n + bin(ii)[2:])[-n:]

        # Initialize two counter variables cnt1 and cnt2
        # cnt1 is used as the index for inserting at the beginning of temp1/2, starts at 0
        cnt1 = 0
        # cnt2 is used as the index for inserting at the end of temp1/2, starts at n-1 (last index)
        cnt2 = n - 1

        # Enumerate over each character 'j' and its index 'k' in the string 'i'
        # 'enumerate(i)' returns (index, character) for each character in the string 'i'
        for k, j in enumerate(i):
            # If the current bit is '1' (as a string, not an integer)
            if j == "1":
                # Place the character from s at position k into temp1 at index cnt1 (from start)
                temp1[cnt1] = s[k]
                # For temp2, place the character from the mirrored position from the end of s
                # 2*n - k - 1 calculates the mirrored index
                temp2[cnt1] = s[2 * n - k - 1]
                # Increment cnt1 to move to the next position from the start
                cnt1 += 1
            else:
                # Place the character from s at position k into temp1 at index cnt2 (from end)
                temp1[cnt2] = s[k]
                # Similarly for temp2, but mirrored index
                temp2[cnt2] = s[2 * n - k - 1]
                # Decrement cnt2 to move to the next position from the end
                cnt2 -= 1

        # Join the elements of temp1 into a string t1
        t1 = "".join(temp1)  # ''.join(list) makes a string from a list of characters

        # Similarly join temp2 into a string t2
        t2 = "".join(temp2)

        # Use tuple (t1, cnt1) as a key in dictionary d1:
        # If the key is not already present, add it with value 1 (first occurrence)
        # Otherwise, increment its count by 1
        if (t1, cnt1) not in d1.keys():
            d1[(t1, cnt1)] = 1
        else:
            d1[(t1, cnt1)] += 1

        # Do the same for d2 with key (t2, cnt1)
        if (t2, cnt1) not in d2.keys():
            d2[(t2, cnt1)] = 1
        else:
            d2[(t2, cnt1)] += 1

    # Initialize a variable ans to 0; this variable will accumulate the final answer
    ans = 0

    # Iterate over each item (key, value pair) in dictionary d1
    # .items() yields (key, value) tuples, where key is (t1, cnt1), value is a count
    for i, j in d1.items():
        # If the current key 'i' exists in d2
        if i in d2.keys():
            # Multiply the count from d1 (j) by the matching count in d2, and add to ans
            ans += j * d2[i]

    # Output the final computed answer using the print function
    print(ans)

# Call the main function to execute the program
main()