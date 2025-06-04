while True:
    try:
        constant_gravity = 9.8
        constant_length = 4.9
        input_velocity = float(raw_input())
        time_fall = input_velocity / constant_gravity
        distance_fallen = constant_length * (time_fall) ** 2
        computed_result = distance_fallen / 5 + 2

        print int(computed_result)

    except EOFError:
        break