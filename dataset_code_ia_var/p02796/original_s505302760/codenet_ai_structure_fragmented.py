def read_number():
    return int(input())

def read_robot():
    x, l = map(int, input().split())
    return x, l

def compute_interval(robot):
    x, l = robot
    return (x - l, x + l)

def read_robots(n):
    robots = []
    for _ in range(n):
        robot = read_robot()
        interval = compute_interval(robot)
        robots.append(interval)
    return robots

def sort_robots_by_end(robots):
    return sorted(robots, key=lambda x: x[1])

def first_robot(robots):
    return robots[0]

def can_place(prev_robot, curr_robot):
    return prev_robot[1] <= curr_robot[0]

def count_non_overlapping_robots(robots):
    count = 1
    prev_robot = first_robot(robots)
    for curr_robot in robots:
        if can_place(prev_robot, curr_robot):
            prev_robot = curr_robot
            count += 1
    return count

def print_result(count):
    print(count)

def main():
    n = read_number()
    robots = read_robots(n)
    sorted_robots = sort_robots_by_end(robots)
    result = count_non_overlapping_robots(sorted_robots)
    print_result(result)

if __name__ == "__main__":
    main()