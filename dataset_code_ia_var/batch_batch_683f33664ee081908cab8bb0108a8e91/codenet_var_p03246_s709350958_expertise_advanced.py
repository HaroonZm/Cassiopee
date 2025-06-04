from collections import Counter

n = int(input())
series = list(map(int, input().split()))

# Use slicing and Counter for efficient frequency counting on odd/even indices
even_counts = Counter(series[::2])
odd_counts = Counter(series[1::2])

# Get top 2 most common (count, value) items for both, filling with (0, None) if needed
even_top = even_counts.most_common(2) + [(0, None)] * (2 - len(even_counts))
odd_top = odd_counts.most_common(2) + [(0, None)] * (2 - len(odd_counts))

(even_cnt1, even_val1), (even_cnt2, even_val2) = even_top
(odd_cnt1, odd_val1), (odd_cnt2, odd_val2) = odd_top

if even_val1 != odd_val1:
    print(n - even_cnt1 - odd_cnt1)
else:
    change1 = n - even_cnt1 - odd_cnt2
    change2 = n - even_cnt2 - odd_cnt1
    # If there's no second most common, its count is 0 – that's fine.
    print(min(change1, change2))