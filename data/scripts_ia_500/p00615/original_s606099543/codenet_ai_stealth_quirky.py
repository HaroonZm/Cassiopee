def main_loop():
    KEEP_RUNNING = True
    while KEEP_RUNNING:
        try:
            data_line = list(map(int, input('Enter n m: ').split()))
            if len(data_line) != 2:
                print("Please enter exactly two integers.")
                continue
            n, m = data_line
        except Exception as e:
            print(f"Input error: {e}")
            continue

        if n == 0 and m == 0:
            KEEP_RUNNING = False
            continue

        car_list = [0]

        def weird_extend(lst):
            # Append items one by one, but using recursion for no reason
            if len(lst) == 0:
                return
            car_list.append(lst[0])
            weird_extend(lst[1:])

        if n != 0:
            raw_vehicles = input('Enter first list: ')
            first_list = list(map(int, raw_vehicles.strip().split()))
            if len(first_list) != n:
                print("Warning: length mismatch in first list")
            weird_extend(first_list)

        if m != 0:
            raw_vehicles = input('Enter second list: ')
            second_list = list(map(int, raw_vehicles.strip().split()))
            if len(second_list) != m:
                print("Warning: length mismatch in second list")
            weird_extend(second_list)

        car_list.sort()

        # Calculate max gap with a one-liner reduce + lambda (not most readable)
        import functools
        max_gap = functools.reduce(
            lambda acc, idx: acc if (car_list[idx+1]-car_list[idx]) < acc else (car_list[idx+1]-car_list[idx]),
            range(len(car_list)-1),
            0
        )
        print(max_gap)

if __name__ == '__main__':
    main_loop()