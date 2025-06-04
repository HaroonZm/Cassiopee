import heapq

def build_frequency_table(s):
    """
    Build a table representing the frequency of each ASCII character in the input string.

    Args:
        s (str): Input string.

    Returns:
        list: A list of size 256 where each element [count, char_code] contains the frequency
              count and its character code (0-255).
    """
    # Initialize an array for counts of all ASCII characters (0-255)
    chars = [[0, n] for n in range(256)]
    # Count each character's occurrence in the string
    for character in s:
        chars[ord(character)][0] += 1
    return chars

def build_huffman_tree(chars):
    """
    Construct the Huffman tree based on the character frequency table.

    Args:
        chars (list): A frequency table of ASCII characters.

    Returns:
        list: The root of the Huffman tree.
    """
    # The heap will contain nodes in the form [count, char_code, left, right, origin]
    counts = []
    for char in chars:
        if char[0] == 0:
            continue  # Skip unused characters
        heapq.heappush(counts, [char[0], char[1], None, None, char])

    # Build the tree by combining two least frequent nodes until only one remains
    while len(counts) > 1:
        a = heapq.heappop(counts)
        b = heapq.heappop(counts)
        # New node: sum of counts; char_code -1 as an internal node sentinel
        heapq.heappush(counts, [a[0] + b[0], -1, a, b])
    # The remaining node is the root
    return heapq.heappop(counts)

def generate_huffman_codes(root):
    """
    Generate Huffman codes for each character by traversing the tree.

    Args:
        root (list): The root node of the Huffman tree.

    Returns:
        dict: Mapping from character to its Huffman code as a binary string.
    """
    codes = {}
    def dfs(node, code):
        """
        Recursively traverse the Huffman tree to assign codes.

        Args:
            node (list): Current node in the Huffman tree.
            code (str): Accumulated binary code string.
        """
        # Internal node: Recurse to left and right children
        if node[1] < 0:
            dfs(node[2], code + "0")
            dfs(node[3], code + "1")
            return
        # Leaf node: Assign the code to the character
        codes[chr(node[1])] = code
    dfs(root, "")
    return codes

def main():
    """
    Read a string from input, build its Huffman encoding, and print the total length
    of the encoded string.
    """

    S = input()
    
    # Step 1: Count frequency of each character
    chars = build_frequency_table(S)

    # Step 2: Construct Huffman tree
    root = build_huffman_tree(chars)

    # Step 3: Generate codes from the Huffman tree
    codes = generate_huffman_codes(root)

    # Step 4: Calculate the total length of the encoded string
    total_length = 0
    for s in S:
        total_length += len(codes[s])

    # Special case: If only one unique character, its encoding length equals its occurrences
    if len(set(S)) == 1:
        print(len(S))
    else:
        print(total_length)

if __name__ == "__main__":
    main()