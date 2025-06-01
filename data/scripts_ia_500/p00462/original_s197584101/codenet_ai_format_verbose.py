import sys
from sys import stdin
from bisect import bisect_right

input = stdin.readline

def main(args):

    while True:

        total_circumference = int(input())
        if total_circumference == 0:
            break

        number_of_checkpoints = int(input())
        number_of_destinations = int(input())

        checkpoint_positions_clockwise = [int(input()) for _ in range(number_of_checkpoints - 1)]
        destination_positions = [int(input()) for _ in range(number_of_destinations)]

        checkpoint_positions_clockwise.append(0)
        checkpoint_positions_clockwise.append(total_circumference)
        checkpoint_positions_clockwise.sort()

        checkpoint_positions_counterclockwise = [total_circumference - pos for pos in checkpoint_positions_clockwise]
        checkpoint_positions_counterclockwise.sort()

        total_min_distance = 0

        for destination in destination_positions:

            if destination == 0:
                continue

            # Find position in clockwise checkpoints
            index_cw = bisect_right(checkpoint_positions_clockwise, destination)
            distance_cw = min(destination - checkpoint_positions_clockwise[index_cw - 1],
                              checkpoint_positions_clockwise[index_cw] - destination)

            # Find position in counterclockwise checkpoints
            counterclockwise_destination = total_circumference - destination
            index_ccw = bisect_right(checkpoint_positions_counterclockwise, counterclockwise_destination)
            distance_ccw = min(counterclockwise_destination - checkpoint_positions_counterclockwise[index_ccw - 1],
                               checkpoint_positions_counterclockwise[index_ccw] - counterclockwise_destination)

            min_distance = min(distance_cw, distance_ccw)
            total_min_distance += min_distance

        print(total_min_distance)


if __name__ == '__main__':
    main(sys.argv[1:])