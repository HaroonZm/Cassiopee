import sys
from sys import stdin
from bisect import bisect_right

input = stdin.readline

def main(args):
    
    while True:
        circle_circumference = int(input())
        if circle_circumference == 0:
            break
        
        number_of_checkpoints = int(input())
        number_of_destinations = int(input())
        
        clockwise_checkpoints = [int(input()) for _ in range(number_of_checkpoints - 1)]
        destination_positions = [int(input()) for _ in range(number_of_destinations)]
        
        # Add start and end of the circle as checkpoints
        clockwise_checkpoints.append(0)
        clockwise_checkpoints.append(circle_circumference)
        clockwise_checkpoints.sort()
        
        total_min_distance = 0
        
        for destination in destination_positions:
            if destination == 0:
                continue
            
            insert_index = bisect_right(clockwise_checkpoints, destination)
            distance_to_prev_checkpoint = destination - clockwise_checkpoints[insert_index - 1]
            distance_to_next_checkpoint = clockwise_checkpoints[insert_index] - destination
            min_distance_to_checkpoint = min(distance_to_prev_checkpoint, distance_to_next_checkpoint)
            
            total_min_distance += min_distance_to_checkpoint
        
        print(total_min_distance)


if __name__ == '__main__':
    main(sys.argv[1:])