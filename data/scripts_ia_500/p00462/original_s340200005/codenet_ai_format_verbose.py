import bisect
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve():
    
    total_distance = int(input())
    if total_distance == 0:
        return False
    
    number_of_stores = int(input())
    number_of_destinations = int(input())
    
    intermediate_store_positions = [int(input()) for _ in range(number_of_stores - 1)]
    
    all_store_positions = [0] + sorted(intermediate_store_positions) + [total_distance]
    
    total_minimum_distance_sum = 0
    
    for _ in range(number_of_destinations):
        destination_position = int(input())
        
        insertion_index = bisect.bisect_right(all_store_positions, destination_position)
        
        distance_to_next_store = all_store_positions[insertion_index] - destination_position
        distance_to_previous_store = destination_position - all_store_positions[insertion_index - 1]
        
        minimum_distance_to_store = min(distance_to_next_store, distance_to_previous_store)
        
        total_minimum_distance_sum += minimum_distance_to_store
    
    return total_minimum_distance_sum


results = []

while True:
    result = solve()
    if result:
        results.append(result)
    else:
        break

print("\n".join(map(str, results)))