# Solution for the "おせんべい" problem.
# 
# Problem summary:
# - We have an R x C grid of senbei cookies.
# - Each cell shows whether the cookie side facing up is "表" (1) or "裏" (0).
# - After earthquake some senbei flipped unexpectedly.
# - We want to flip rows (0 or more) and then flip columns (0 or more) so that the maximum number of cookies are in the state "裏" (0) after the flips.
# - Each flipping operation toggles all senbei in the chosen rows/columns.
# - Flips are done first on any subset of rows simultaneously, then on any subset of columns simultaneously.
# - We want to maximize the number of cookies that have "裏"(0) side showing after these flips.
# - R ≤ 10; C ≤ 10,000
#
# Key points:
# - Because R is small and C is large, we process column-wise.
# - For each column, the pattern of that column’s cells can be represented as an R-bit integer (for R rows).
# - For an initial pattern S of length R bits for a column:
#   After flipping some rows (subset X), the column pattern becomes S XOR X.
#   Then, after flipping some columns, the column can be toggled: but here columns flips are done after rows flips,
#   and columns flips toggle the bits in the entire column. But columns flips toggle some columns, not bits inside a column.
# - After flipping rows, the column patterns can be compared.
# - Then flipping columns corresponds to toggling particular columns entirely, i.e., the entire column is toggled.
#
# Since flipping columns toggles all bits in that column:
# - For a given pattern P (resulting after row flips), flipping the whole column toggles bits: P' = P ^ mask of all ones (bitwise negation).
# - Our problem reduces to choosing a rows flipping mask X to maximize the total count of zeros after flips over columns and possible flip of that column.
#
# The approach:
# 1. Encode each column as an R-bit pattern (0 or 1 per row).
# 2. For each possible rows flips mask X (0 <= X < 2^R):
#    - For each distinct column pattern S with frequency freq:
#      - Calculate the pattern after flipping rows: S' = S XOR X.
#      - Count the number of zeros in S' (count0), and ones in S' (count1 = R - count0).
#      - For this column, after flipping rows, we can either flip this column or not:
#          - Not flip => zeros = count0
#          - Flip column => zeros = count1
#      - Choose max of above two.
#    - Sum over all column patterns weighted by their frequency.
#    - Keep the maximum sum over all X.
#
# Implement details:
# - Precompute popcount for each R-bit integer.
# - Use dictionaries to count column patterns frequencies.
# - Iterate over all 2^R row flips masks.
# 
# This will be efficient enough given R <= 10.

import sys

def main():
    input = sys.stdin.readline

    while True:
        R, C = map(int, input().split())
        if R == 0 and C == 0:
            break

        # Read grid and encode each column as a bit pattern (R bits)
        # bit 0 corresponds to row 0, bit R-1 to row R-1
        # Because input is row-wise, we build columns by reading rows
        col_patterns = [0]*C
        for r in range(R):
            row_values = list(map(int, input().split()))
            for c in range(C):
                if row_values[c] == 1:
                    # set bit r in column c
                    col_patterns[c] |= (1 << r)

        # Count frequency of each column pattern
        freq = {}
        for p in col_patterns:
            freq[p] = freq.get(p, 0) + 1

        # Precompute popcount for integers 0 to 2^R - 1
        max_mask = 1 << R
        popcount = [0]*(max_mask)
        for i in range(max_mask):
            popcount[i] = popcount[i >> 1] + (i & 1)

        max_zeroes = 0

        # Try all possible row flip masks
        for row_flip_mask in range(max_mask):
            total_zeroes = 0
            for pattern, count_col in freq.items():
                flipped_pattern = pattern ^ row_flip_mask
                count_ones = popcount[flipped_pattern]
                count_zeros = R - count_ones
                # flip column or not, choose max zeros
                max_zeros_col = max(count_zeros, count_ones)
                total_zeroes += max_zeros_col * count_col

            if total_zeroes > max_zeroes:
                max_zeroes = total_zeroes

        print(max_zeroes)

if __name__ == '__main__':
    main()