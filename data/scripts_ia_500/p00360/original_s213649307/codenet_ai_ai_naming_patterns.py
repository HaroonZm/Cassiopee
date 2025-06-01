from bisect import bisect_left as binary_search_left

def execute():
    character_codes = list(map(ord, list(input())))
    budget = int(input())
    selected_characters = []
    selected_positions = []
    position_map = {}
    ordinal_a = ord("a")
    ordinal_z = ord("z")
    for index, code in enumerate(character_codes):
        if code in position_map:
            position_map[code].append(index)
        else:
            position_map[code] = [index]
    sorted_keys = sorted(position_map.keys())
    for key in sorted_keys:
        position_map[key].reverse()
    
    while budget:
        for key in sorted_keys:
            initial_position = position_map[key][-1]
            prior_selected_count = binary_search_left(selected_positions, initial_position)
            cost = initial_position - prior_selected_count
            if cost <= budget:
                budget -= cost
                selected_characters.append(key)
                insert_position = binary_search_left(selected_positions, initial_position)
                selected_positions.insert(insert_position, initial_position)
                position_map[key].pop()
                if not position_map[key]:
                    sorted_keys.remove(key)
                break
        else:
            break
    
    selected_positions.sort(reverse=True)
    for position in selected_positions:
        character_codes.pop(position)
    print("".join(map(chr, selected_characters + character_codes)))

execute()