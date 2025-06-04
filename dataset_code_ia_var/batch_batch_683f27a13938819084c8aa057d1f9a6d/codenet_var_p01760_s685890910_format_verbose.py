total_time_required, total_distance_required = map(int, input().split())
time_per_unit_a, time_per_unit_b = map(int, input().split())
distance_per_unit_a, distance_per_unit_b = map(int, input().split())

minimum_time_difference = 10000000007

for count_a in range(total_distance_required // distance_per_unit_a + 1):
    
    for count_b in range(total_distance_required // distance_per_unit_b + 1):
        
        distance_covered_a = count_a * distance_per_unit_a
        distance_covered_b = count_b * distance_per_unit_b
        total_distance_covered = distance_covered_a + distance_covered_b
        
        if 1 <= total_distance_covered <= total_distance_required:
            
            total_time_taken_a = time_per_unit_a * distance_covered_a
            total_time_taken_b = time_per_unit_b * distance_covered_b
            weighted_average_time = (total_time_taken_a + total_time_taken_b) / total_distance_covered
            
            time_difference = abs(total_time_required - weighted_average_time)
            
            minimum_time_difference = min(minimum_time_difference, time_difference)

print(minimum_time_difference)