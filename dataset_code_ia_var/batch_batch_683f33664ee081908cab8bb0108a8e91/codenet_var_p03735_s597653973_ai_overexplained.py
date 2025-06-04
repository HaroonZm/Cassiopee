import sys  # Import the sys module to use sys.stdin for reading input.
from operator import itemgetter  # Import itemgetter to allow sorting by tuple elements.

# Define a large constant to represent infinity for initial minimum comparisons.
inf = 1 << 30  # This is equivalent to 2^30, which is a very large integer value.

def solve():
    # Read one line from standard input, strip spaces and newlines,
    # convert it to integer type, and assign to n.
    n = int(sys.stdin.readline())

    # Initialize variables to store the maximum and minimum values.
    # r_max, b_max represent the maximum values seen so far for y and x coordinates respectively.
    # r_min, b_min represent the minimum values seen so far for y and x coordinates.
    # They start at 0 for max (since all actual values should be >=0),
    # and at inf for min to ensure any real input will be smaller.
    r_max = 0  # Largest y-value found so far.
    b_max = 0  # Largest x-value found so far.
    r_min = inf  # Smallest y-value found so far.
    b_min = inf  # Smallest x-value found so far.

    p = []  # An array to store pairs (x, y).

    # Iterate n times to read n pairs of integer coordinates.
    for i in range(n):
        # Read a line from standard input, split it into two elements,
        # convert them from strings to integers,
        # and unpack them into variables xi and yi.
        xi, yi = map(int, sys.stdin.readline().split())

        # If xi is greater than yi, swap them to ensure (xi, yi) are sorted so xi <= yi.
        if xi > yi:
            xi, yi = yi, xi

        # Add the tuple (xi, yi) to list p.
        p.append((xi, yi))

        # Update the maximum y-value seen so far.
        r_max = max(r_max, yi)
        # Update the minimum y-value seen so far.
        r_min = min(r_min, yi)
        # Update the maximum x-value seen so far.
        b_max = max(b_max, xi)
        # Update the minimum x-value seen so far.
        b_min = min(b_min, xi)

    # Calculate the area of the rectangle that covers
    # all the input points, using the max and min y and x.
    # (r_max - r_min) is the height, (b_max - b_min) is the width.
    # Multiply them to get the area.
    ans1 = (r_max - r_min) * (b_max - b_min)

    # Calculate another candidate answer.
    # The difference (r_max - b_min) represents possibly the maximal y minus minimal x,
    # considering a different way to enclose points.
    ans2 = (r_max - b_min)

    # Sort the list p, which contains coordinate pairs,
    # by the first element (x) of each tuple, in ascending order.
    # This is needed for the next part of the algorithm.
    p.sort(key=itemgetter(0))

    # After sorting, the first element of the list has the smallest x,
    # and the last element has the largest x.
    b_min = p[0][0]  # Smallest x value among points after sorting.
    b_max = p[-1][0]  # Largest x value among points after sorting.

    y_min = inf  # Initialize y_min to inf to find the smallest y-value seen in the loop below.

    # dif_b will store the minimum possible difference found later.
    dif_b = b_max - b_min  # Start with the initial x-range.

    # Loop to find a possibly smaller width for the area, while investigating y-values.
    # Go through all pairs except the very last one.
    for i in range(n - 1):
        # If the current y-value equals the largest y-value seen in all of p, stop the loop,
        # as the following calculations are not valid beyond this point.
        if p[i][1] == r_max:
            break
        # Update y_min to hold the smallest y seen so far up to this point in the loop.
        y_min = min(y_min, p[i][1])

        # Update b_min to be the smaller of the next x value and y_min.
        # This tries to find a possible partitioning that makes the width smaller.
        b_min = min(p[i + 1][0], y_min)
        # Update b_max to be the larger of the previous b_max and the current y value.
        b_max = max(b_max, p[i][1])

        # Update dif_b to be the smaller of its current value and the difference (b_max - b_min).
        dif_b = min(dif_b, b_max - b_min)

    # Multiply the height (r_max - b_min, previously calculated in ans2) by the minimized width dif_b.
    ans2 *= dif_b

    # The final answer is the smaller of the two candidate areas.
    ans = min(ans1, ans2)

    # Output the final answer to standard output.
    print(ans)

# The standard way to ensure the solve() function only runs when this script
# is executed directly, not when it is imported as a module.
if __name__ == '__main__':
    solve()