row_count, col_count, pair_count = map(int, input().split())
pair_scores = [None] * pair_count
for pair_index in range(pair_count):
    row_index, col_index = map(int, input().split())
    if col_index <= col_count:
        col_index -= 1
    pair_scores[pair_index] = row_count + 1 - row_index + abs(col_count - col_index)
max_score = 0
for sorted_index, score in enumerate(sorted(pair_scores, reverse=True)):
    max_score = max(max_score, sorted_index + score)
print(max_score)