from collections import deque

def new_color(s, i, color):
    """
    Replace two consecutive characters in the string `s` starting at index `i`
    with two occurrences of the specified `color`.
    
    Args:
        s (str): The original string representing colors.
        i (int): The starting index of the pair to replace.
        color (str): The color to replace the pair with (a single character).
    
    Returns:
        str: A new string with the specified pair replaced by `color * 2`.
    """
    # Replace characters at positions i and i+1 with the new color repeated twice
    return s[:i] + color * 2 + s[i + 2:]

def solve(s):
    """
    Determine the minimum number of operations needed to convert the string `s`
    into a monochromatic string (all characters the same), where an operation consists
    of replacing two adjacent different colors by two of the third color.
    
    The colors involved are 'r', 'g', and 'b'. The operation replaces any differing pair 
    of adjacent colors with two instances of the color that is not in the pair.

    For example:
        - 'r' and 'g' -> 'b'
        - 'r' and 'b' -> 'g'
        - 'g' and 'b' -> 'r'

    Args:
        s (str): The input string representing a sequence of colors.
    
    Prints:
        int or 'NA': The minimum number of operations to achieve monochromaticity, 
                     or 'NA' if impossible.
    """
    length = len(s)
    # List of all possible monochromatic strings with the same length as s
    monos = ["r" * length, "g" * length, "b" * length]

    # If s is already monochromatic, no operation needed
    if s in monos:
        print(0)
        return

    # Mapping pairs of different colors to the remaining third color
    rgb = "rgb"
    another = {
        ("r", "g"): "b", ("g", "r"): "b",
        ("r", "b"): "g", ("b", "r"): "g",
        ("g", "b"): "r", ("b", "g"): "r"
    }

    # Dictionary to store strings visited and their operation counts
    dic = {s: 0}
    # Queue for BFS traversal of states (string variants)
    que = deque()
    que.append((s, 0))

    while que:
        colors, score = que.popleft()
        # Increment score because we consider the next operation
        score += 1
        temp = colors[0]

        # Iterate over pairs of adjacent colors
        for i in range(1, length):
            ci = colors[i]
            # If adjacent colors differ
            if ci != temp:
                # Create a new string with the current differing pair replaced
                new = new_color(colors, i - 1, another[(ci, temp)])

                # If new string is monochromatic, print result and return
                if new in monos:
                    print(score)
                    return

                # If new string was not visited, append to the queue
                if new not in dic:
                    dic[new] = score
                    que.append((new, score))

            temp = ci

    # If queue is exhausted and no monochromatic string found, print 'NA'
    print("NA")

def main():
    """
    Main function to repeatedly read input strings representing sequences of colors,
    and call `solve()` on each until an input of '0' is encountered, which terminates
    the program.
    """
    while True:
        s = input()
        # Exit condition
        if s == "0":
            break
        # Process the current input string
        solve(s)

main()