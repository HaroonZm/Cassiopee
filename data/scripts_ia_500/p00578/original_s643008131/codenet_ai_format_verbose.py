def solve():
    
    number_of_points = int(input())
    
    height_list_with_boundaries = [0] + [int(height) for height in input().split()] + [0]
    
    edge_points = []
    
    is_ascending = True
    
    for current_index in range(1, len(height_list_with_boundaries) - 1):
        
        current_height = height_list_with_boundaries[current_index]
        next_height = height_list_with_boundaries[current_index + 1]
        
        if is_ascending:
            if current_height > next_height:
                edge_points.append([current_height, is_ascending])
                is_ascending = not is_ascending
        else:
            if current_height < next_height:
                edge_points.append([current_height, is_ascending])
                is_ascending = not is_ascending
                
    edge_points.sort()
    
    current_island_count = 1
    maximum_island_count = 1
    
    for index in range(len(edge_points) - 1):
        
        height_value, ascending_flag = edge_points[index]
        
        if ascending_flag:
            current_island_count -= 1
        else:
            current_island_count += 1
            
        next_height_value = edge_points[index + 1][0]
        
        if height_value < next_height_value:
            maximum_island_count = max(maximum_island_count, current_island_count)
            
    if max(height_list_with_boundaries) <= 0:
        maximum_island_count = 0
        
    print(maximum_island_count)
    

if __name__ == '__main__':
    solve()