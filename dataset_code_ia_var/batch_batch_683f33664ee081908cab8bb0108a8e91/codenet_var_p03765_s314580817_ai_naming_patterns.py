def process_strings_and_queries():
    source_sequence = list(str(input()))
    target_sequence = list(str(input()))
    num_queries = int(input())
    source_cumulative = [0]
    target_cumulative = [0]
    for character in source_sequence:
        if character == "A":
            source_cumulative.append((source_cumulative[-1] + 1) % 3)
        else:
            source_cumulative.append((source_cumulative[-1] + 2) % 3)
    for character in target_sequence:
        if character == "A":
            target_cumulative.append((target_cumulative[-1] + 1) % 3)
        else:
            target_cumulative.append((target_cumulative[-1] + 2) % 3)
    for _ in range(num_queries):
        source_left, source_right, target_left, target_right = map(int, input().split())
        source_difference = source_cumulative[source_right] - source_cumulative[source_left - 1]
        target_difference = target_cumulative[target_right] - target_cumulative[target_left - 1]
        if source_difference % 3 == target_difference % 3:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    process_strings_and_queries()