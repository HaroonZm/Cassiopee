class FenwickTree:
    def __init__(self, length):
        self.length = length
        self.data = [0] * (length + 1)

    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.data[index]
            index -= index & -index
        return total

    def add_value(self, index, value):
        while index <= self.length:
            self.data[index] += value
            index += index & -index

input_size, query_count = map(int, input().split())
fenwick_tree = FenwickTree(input_size + 1)
city_sequence = map(int, input().split())
previous_city = next(city_sequence)

for current_city in city_sequence:
    if previous_city < current_city:
        fenwick_tree.add_value(previous_city, 1)
        fenwick_tree.add_value(current_city, -1)
    else:
        fenwick_tree.add_value(current_city, 1)
        fenwick_tree.add_value(previous_city, -1)
    previous_city = current_city

total_cost = 0
for position in range(1, input_size):
    cost_high, cost_low, penalty = map(int, input().split())
    threshold = penalty // (cost_high - cost_low)
    count = fenwick_tree.prefix_sum(position)
    if count > threshold:
        total_cost += cost_low * count + penalty
    else:
        total_cost += cost_high * count

print(total_cost)