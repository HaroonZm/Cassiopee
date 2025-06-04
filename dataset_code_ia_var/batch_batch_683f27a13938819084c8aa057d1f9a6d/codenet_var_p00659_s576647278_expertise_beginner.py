import itertools

while True:
    n = int(input())
    if n == 0:
        break

    data = {}
    names = []
    for i in range(n):
        line = input().split()
        name = line[0]
        cars = line[2:]
        data[name] = cars
        names.append(name)

    others_cars = {}
    for group in itertools.combinations(list(data.items()), n-1):
        group_names = []
        group_cars = []
        for name, cars in group:
            group_names.append(name)
            group_cars += cars
        for name in names:
            if name not in group_names:
                others_cars[name] = group_cars
                break

    results = {}
    for name in data:
        count = 0
        for car in data[name]:
            count += n - others_cars[name].count(car)
        results[name] = count

    sorted_results = sorted(results.items(), key=lambda x: (x[1], x[0]))
    answer_name, answer_count = sorted_results[0][0], sorted_results[0][1]
    print(answer_count, answer_name)