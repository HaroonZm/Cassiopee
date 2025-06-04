import math

def in_obstacle(x, y, obstacles):
    for (L, B, R, T) in obstacles:
        if L <= x <= R and B <= y <= T:
            return True
    return False

def bird_position(V, angle, t):
    g = 9.8
    x = V * math.cos(angle) * t
    y = V * math.sin(angle) * t - 0.5 * g * t * t
    return x, y

def egg_can_hit_pig(V, X, Y, obstacles):
    g = 9.8
    # Try angles from 0 to pi/2 with small steps
    for deg in range(1, 90):
        angle = math.radians(deg)
        t_end = 2 * V * math.sin(angle) / g  # total flight time until y=0
        t = 0
        step = 0.01
        can_drop = True
        drop_positions = []
        while t <= t_end:
            x, y = bird_position(V, angle, t)
            if y < 0:
                break
            if in_obstacle(x, y, obstacles):
                can_drop = False
                break
            t += step
        if not can_drop:
            continue
        # If can_drop is True, try to drop egg at some time t_drop
        t = 0
        while t <= t_end:
            x_bird, y_bird = bird_position(V, angle, t)
            if y_bird < 0:
                break
            # Check if bird is inside any obstacle
            if in_obstacle(x_bird, y_bird, obstacles):
                t += step
                continue
            # Egg falls straight down from (x_bird, y_bird)
            # Check if egg hits pig at (X, Y)
            if abs(x_bird - X) > 0.01:
                t += step
                continue
            if y_bird < Y:
                t += step
                continue
            # Egg falls from y_bird to Y, check if any obstacle in between at x_bird
            hit_obstacle = False
            for (L, B, R, T) in obstacles:
                if L <= x_bird <= R:
                    if B <= Y <= T:
                        hit_obstacle = True
                        break
                    if Y <= B <= y_bird:
                        hit_obstacle = True
                        break
            if hit_obstacle:
                t += step
                continue
            # Egg can reach pig without obstacles
            return True
            t += step
    return False

def main():
    N, V, X, Y = map(int, input().split())
    obstacles = []
    for _ in range(N):
        L, B, R, T = map(int, input().split())
        obstacles.append((L, B, R, T))
    if egg_can_hit_pig(V, X, Y, obstacles):
        print("Yes")
    else:
        print("No")

main()