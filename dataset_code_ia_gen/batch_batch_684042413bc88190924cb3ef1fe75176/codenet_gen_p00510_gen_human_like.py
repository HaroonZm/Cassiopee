n = int(input())
m = int(input())
cars_in_tunnel = m
max_cars = m
error = False

for _ in range(n):
    entered, exited = map(int, input().split())
    cars_in_tunnel += entered - exited
    if cars_in_tunnel < 0:
        error = True
    if cars_in_tunnel > max_cars:
        max_cars = cars_in_tunnel

if error:
    print(0)
else:
    print(max_cars)