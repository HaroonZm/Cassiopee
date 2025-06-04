number_of_tanks = int(input())

tank_capacities = [int(capacity) for capacity in input().split()]

current_tank_volumes = [0] * number_of_tanks

number_of_queries = int(input())

for _ in range(number_of_queries):

    query_type, tank_index, volume_delta = map(int, input().split())
    tank_position = tank_index - 1

    if query_type == 1:

        current_tank_volumes[tank_position] = current_tank_volumes[tank_position] + volume_delta

        if current_tank_volumes[tank_position] > tank_capacities[tank_position]:

            print(tank_index)
            exit()

    if query_type == 2:

        current_tank_volumes[tank_position] = current_tank_volumes[tank_position] - volume_delta

        if current_tank_volumes[tank_position] < 0:

            print(tank_index)
            exit()

print(0)