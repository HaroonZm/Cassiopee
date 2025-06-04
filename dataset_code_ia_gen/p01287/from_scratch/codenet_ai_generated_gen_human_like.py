import sys
from math import factorial
from collections import Counter

def permutations_count(n, counts):
    # Calculate number of distinct permutations of n elements with given counts
    result = factorial(n)
    for c in counts:
        result //= factorial(c)
    return result

# We use Burnside's lemma to count distinct colorings up to the octahedron's rotational symmetry group.
# The rotational symmetry group of octahedron has 24 elements.

# Cycle structures of the rotational symmetry group acting on 8 triangular faces:
# List of (number of elements in conjugacy class, cycle structure as list of cycle lengths)
# Source: group theory of octahedron face permutations
# Reference cycles for the action on 8 faces:
# Class sizes and corresponding face cycle types
# identities: 1 element, 8 cycles of length 1
# 6 rotations 180° about axes through midpoints of opposite edges: 6 elements, cycle type [2,2,2,2]
# 3 rotations 180° about axes through midpoints of opposite faces: 3 elements, cycle type [4,4]
# 8 rotations 120° about axes through opposite vertices: 8 elements, cycle type [3,3,2]
# 6 rotations 90° and 270° about axes through opposite faces: 6 elements, cycle type [4,2,1,1]

# Cycle structures summarized as (count, cycle lengths):
rotation_classes = [
    (1,  [1,1,1,1,1,1,1,1]),    # identity
    (6,  [2,2,2,2]),            # 180° edge rotations
    (3,  [4,4]),                # 180° face rotations
    (8,  [3,3,2]),              # 120° vertex rotations
    (6,  [4,2,1,1])             # 90° and 270° face rotations
]

def count_fixed_colorings(color_count, cycle_lengths):
    # Counts number of colorings fixed by a group element with given cycle lengths.
    # A coloring is fixed if for each cycle all positions have same color
    # Since we must assign colors to cycles, and each cycle can be assigned any color, the color count distribution must be compatible.
    # For the panel colors, the total number of cycles is len(cycle_lengths)
    #
    # To count colorings fixed by symmetry:
    # For each cycle of length l, the color assigned to it appears l times.
    # So the multiset of color counts must be decomposable into groups of size equal to the cycle lengths.
    #
    # So we must count how many ways to assign colors to cycles so that sum of cycles assigned per color * cycle length = color count

    # The problem reduces to: Is it possible to partition the color count into sums of cycle lengths?
    # Because the order of cycles is fixed and indistinguishable within groupings, the count is:
    # Number of ways to assign colors to cycles where each color ci is assigned cycles summing to count_i / cycle_length

    # We transform the problem into integer partition to avoid combinatoric explosion:
    # Since cycle lengths vary, for each color, number_color_of_cycles = color_count[color] // cycle_length, and color_count[color] % cycle_length == 0 must hold

    lcm = 1
    for l in cycle_lengths:
        # lcm of cycle lengths could be useful, but here probably not needed
        pass

    # Generally the cycle lengths might have multiple lengths, so must check feasibility
    # We will use a backtracking approach to assign cycles to colors
    # But since number of cycles is small, we can proceed:

    # The approach:
    # The cycles are identical except for length; all cycles with same length are indistinguishable.
    # Group cycles by length
    from collections import defaultdict
    cycles_by_length = defaultdict(int)
    for c_len in cycle_lengths:
        cycles_by_length[c_len] +=1

    # Now, for each color with count col_count, it must be representable as sum over lengths l of cycles of l * x_l where x_l are integers <= cycles_by_length[l]
    # The sum over all colors x_l for each l must equal to total number of cycles of length l

    # This is a system of equations:
    # For each length l: sum over colors of x_l(color) = cycles_by_length[l]
    # For each color c: sum over lengths l of x_l(c)*l = col_count
    # x_l(c) >= 0 integer

    # Solve using integer linear programming or backtracking. Because small, backtrack.


    lengths = list(cycles_by_length.keys())
    total_cycles_per_length = [cycles_by_length[l] for l in lengths]
    colors = list(color_count.keys())
    color_values = [color_count[c] for c in colors]

    # x: colors x lengths matrix to find (x[color][length])

    n_colors = len(colors)
    n_lengths = len(lengths)

    # backtracking function
    def backtrack(i, remaining_cycles, assigned):
        # i: color index
        # remaining_cycles: list of remaining cycles counts for each length
        # assigned: matrix [color][length] so far

        if i == n_colors:
            # check if all cycles assigned
            return all(r == 0 for r in remaining_cycles)
        col_need = color_values[i]
        # For this color, try all possible assignments of cycles per length such that sum(x * length) = col_need and x <= remaining_cycles
        # x_i are integers >=0

        # Generate all combinations for this color

        results = 0

        def assign_cycle_counts(pos, chosen, sum_len):
            if pos == n_lengths:
                if sum_len == col_need:
                    # Check if chosen <= remaining_cycles
                    for idx in range(n_lengths):
                        if chosen[idx] > remaining_cycles[idx]:
                            return
                    # assign chosen
                    new_remaining = [remaining_cycles[j] - chosen[j] for j in range(n_lengths)]
                    assigned[i] = chosen[:]
                    nonlocal results
                    res = backtrack(i+1, new_remaining, assigned)
                    results += res
                return
            max_count = min(remaining_cycles[pos], col_need // lengths[pos])
            for cnt in range(max_count+1):
                new_sum = sum_len + cnt*lengths[pos]
                if new_sum <= col_need:
                    chosen.append(cnt)
                    assign_cycle_counts(pos+1, chosen, new_sum)
                    chosen.pop()
                else:
                    break

        assign_cycle_counts(0, [], 0)
        return results

    assigned = [[0]*n_lengths for _ in range(n_colors)]

    return backtrack(0, total_cycles_per_length, assigned)

def main():
    lines = sys.stdin.read().split()
    # datasets: each 8 colors
    for i in range(0, len(lines), 8):
        colors = lines[i:i+8]
        color_count = Counter(colors)

        total = 0
        for class_size, cycle_lengths in rotation_classes:
            fixed = count_fixed_colorings(color_count, cycle_lengths)
            total += class_size * fixed
        # number of distinct colorings = total / |G| = total / 24
        print(total // 24)

if __name__=="__main__":
    main()