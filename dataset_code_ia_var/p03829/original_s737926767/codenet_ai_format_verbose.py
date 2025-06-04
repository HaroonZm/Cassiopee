import sys

try:
    from typing import List
except ImportError:
    pass

def compute_minimum_total_cost(
    number_of_stations: int,
    cost_per_distance_unit: int,
    maximum_flat_cost: int,
    station_positions: "List[int]"
):
    total_minimum_cost = sum(
        min(
            (next_station_position - current_station_position) * cost_per_distance_unit,
            maximum_flat_cost
        )
        for current_station_position, next_station_position in zip(
            station_positions, station_positions[1:]
        )
    )
    print(total_minimum_cost)

def parse_input_and_execute():
    def input_word_generator():
        for input_line in sys.stdin:
            for word in input_line.split():
                yield word

    input_words = input_word_generator()

    total_number_of_stations = int(next(input_words))
    distance_cost_per_unit = int(next(input_words))
    maximum_cost_per_move = int(next(input_words))
    station_coordinates_list = [
        int(next(input_words)) for _ in range(total_number_of_stations)
    ]

    compute_minimum_total_cost(
        total_number_of_stations,
        distance_cost_per_unit,
        maximum_cost_per_move,
        station_coordinates_list
    )

if __name__ == '__main__':
    parse_input_and_execute()