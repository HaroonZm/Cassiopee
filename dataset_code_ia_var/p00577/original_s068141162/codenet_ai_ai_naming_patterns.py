input_length = int(input())
input_chars = list(input().strip())

index_current = 0
index_next = 1
pair_count = 0

while index_current < input_length:
    if index_current < input_length - 1:
        if input_chars[index_current] != input_chars[index_next]:
            pair_count += 1
            index_current += 2
            index_next += 2
        else:
            index_current += 1
            index_next += 1
            continue
    else:
        index_current += 1

print(pair_count)