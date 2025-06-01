INF = 0x7fffffff

number_of_cards = int(input())

minimum_cost = [[INF for end_index in range(number_of_cards)] for start_index in range(number_of_cards)]

card_dimensions = [[0 for dimension_index in range(2)] for card_index in range(number_of_cards)]

for card_index in range(number_of_cards):
    minimum_cost[card_index][card_index] = 0

for card_index in range(number_of_cards):
    card_dimensions[card_index][0], card_dimensions[card_index][1] = map(int, input().split())

for subsequence_length in range(1, number_of_cards):
    for start_index in range(number_of_cards - subsequence_length):
        end_index = start_index + subsequence_length
        for split_point in range(start_index, end_index):
            cost_of_splitting = (
                minimum_cost[start_index][split_point]
                + card_dimensions[start_index][0]
                * card_dimensions[split_point][1]
                * card_dimensions[split_point + 1][0]
                * card_dimensions[end_index][1]
                + minimum_cost[split_point + 1][end_index]
            )
            if cost_of_splitting < minimum_cost[start_index][end_index]:
                minimum_cost[start_index][end_index] = cost_of_splitting

print(minimum_cost[0][number_of_cards - 1])