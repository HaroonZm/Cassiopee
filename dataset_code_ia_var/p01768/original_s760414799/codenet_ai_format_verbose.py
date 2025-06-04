number_of_items = int(input())

item_name_to_index = {}
item_price_list = []

for item_index in range(number_of_items):
    item_name, item_price = input().split()
    item_name_to_index[item_name] = item_index
    item_price_list.append(int(item_price))

disjoint_set_parent = [index for index in range(number_of_items)]

def find_representative(item_index):
    if disjoint_set_parent[item_index] == item_index:
        return item_index
    disjoint_set_parent[item_index] = find_representative(disjoint_set_parent[item_index])
    return disjoint_set_parent[item_index]

number_of_merge_operations = int(input())

for _ in range(number_of_merge_operations):
    item_name_a, item_name_b = input().split()
    index_a = item_name_to_index[item_name_a]
    index_b = item_name_to_index[item_name_b]
    representative_a = find_representative(index_a)
    representative_b = find_representative(index_b)
    disjoint_set_parent[representative_a] = disjoint_set_parent[representative_b]

group_min_price_and_count = {}

for item_index in range(number_of_items):

    group_representative = find_representative(item_index)

    if group_representative in group_min_price_and_count:
        current_min_price, current_count = group_min_price_and_count[group_representative]
        updated_min_price = min(current_min_price, item_price_list[item_index])
        group_min_price_and_count[group_representative] = (updated_min_price, current_count + 1)
    else:
        group_min_price_and_count[group_representative] = (item_price_list[item_index], 1)

total_cost = sum(
    min_price * group_count
    for min_price, group_count in group_min_price_and_count.values()
)

print(total_cost)