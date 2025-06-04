read_line = input
raw_expr = read_line()
tokens = read_line().split('+')
unique_tokens = set(tokens)
token_counts = [tokens.count(token) for token in unique_tokens]
unique_counts = set(token_counts)
result = sum(min(3 * token_counts.count(count), token_counts.count(count) + 4) for count in unique_counts if count != 1)
result += len(token_counts) - 1 + token_counts.count(1)
print(result)