def get_number_of_houses():
    return int(input())

def get_house_positions(n):
    return list(map(int, input().split()))

def calculate_distances(houses, point):
    distances = []
    for house in houses:
        distances.append(abs(house - point))
    return distances

def max_distance(distances):
    max_dist = distances[0]
    for dist in distances:
        if dist > max_dist:
            max_dist = dist
    return max_dist

def update_minimum(current_min, candidate):
    if candidate < current_min:
        return candidate
    else:
        return current_min

def main():
    n = get_number_of_houses()
    houses = get_house_positions(n)
    min_distance = 10000
    for position in range(2001):
        distances = calculate_distances(houses, position)
        max_dist = max_distance(distances)
        min_distance = update_minimum(min_distance, max_dist)
    print(min_distance)

main()