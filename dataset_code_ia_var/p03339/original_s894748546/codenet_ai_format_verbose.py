def main():
    number_of_people_in_line = int(input())
    directions_string = input()
    
    total_east_direction_count = directions_string.count('E')
    total_west_direction_count = 0
    
    minimum_turns_required = total_east_direction_count
    
    for direction in directions_string:
        if direction == 'E':
            total_east_direction_count -= 1
        else:
            total_west_direction_count += 1
        
        current_turns_required = total_east_direction_count + total_west_direction_count
        
        if minimum_turns_required > current_turns_required:
            minimum_turns_required = current_turns_required
    
    print(minimum_turns_required)

if __name__ == '__main__':
    main()