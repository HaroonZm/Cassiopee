bitmask_a = 65280
bitmask_b = 61680
bitmask_c = 52428
bitmask_d = 43690
target_bitmask = 65535

from heapq import heappush, heappop

priority_queue = [
    (1, bitmask_a),
    (1, bitmask_b),
    (1, bitmask_c),
    (1, bitmask_d)
]

minimum_costs = {
    bitmask_a: 1,
    bitmask_b: 1,
    bitmask_c: 1,
    bitmask_d: 1,
    target_bitmask: 1,
    0: 1
}

history_pairs = []

get_min_cost = minimum_costs.get
add_pair_to_history = history_pairs.append

while priority_queue:
    current_cost, current_bitmask = heappop(priority_queue)

    if minimum_costs[current_bitmask] < current_cost:
        continue

    alternate_bitmask = current_bitmask ^ target_bitmask
    if current_cost + 1 < get_min_cost(alternate_bitmask, 17):
        minimum_costs[alternate_bitmask] = current_cost + 1
        if current_cost < 15:
            heappush(priority_queue, (current_cost + 1, alternate_bitmask))

    if current_cost < 13:
        cost_difference = 13 - current_cost
        new_composed_cost = 3 + current_cost
        for history_bitmask, history_cost in history_pairs:
            if history_cost <= cost_difference:
                and_combined = current_bitmask & history_bitmask
                if history_cost < get_min_cost(and_combined, 17) - new_composed_cost:
                    minimum_costs[and_combined] = new_composed_cost + history_cost
                    if history_cost < cost_difference:
                        heappush(priority_queue, (new_composed_cost + history_cost, and_combined))

                xor_combined = current_bitmask ^ history_bitmask
                if history_cost < get_min_cost(xor_combined, 17) - new_composed_cost:
                    minimum_costs[xor_combined] = new_composed_cost + history_cost
                    if history_cost < cost_difference:
                        heappush(priority_queue, (new_composed_cost + history_cost, xor_combined))
            else:
                break

    if current_cost < 7:
        add_pair_to_history((current_bitmask, current_cost))

import sys
user_input = sys.stdin.read()
user_input = user_input.replace('-', '~').replace('*', '&').replace('1', 'e')
bitmask_strings = user_input.split()[:-1]
bitmask_expressions = "target_bitmask&" + ",target_bitmask&".join(bitmask_strings)
bitmask_values = eval(bitmask_expressions)

for bitmask in map(minimum_costs.__getitem__, bitmask_values):
    print(bitmask)