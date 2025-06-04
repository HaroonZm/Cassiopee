import math
import sys

g = 9.8

def inside_obstacle(x, y, obstacles):
    for (L, B, R, T) in obstacles:
        if L <= x <= R and B <= y <= T:
            return True
    return False

def collides_with_obstacle_trajectory(V, angle, obstacles, X):
    # Check if bird trajectory hits any obstacle before reaching x = X
    # Sample x from 0 to X in small steps to check y
    steps = 500
    for i in range(1, steps+1):
        x = X * i / steps
        t = x / (V * math.cos(angle))
        y = V * math.sin(angle) * t - 0.5 * g * t*t
        if y < 0:
            return True
        if inside_obstacle(x, y, obstacles):
            return True
    return False

def can_reach_pig(V, X, Y, obstacles):
    # The white bird launches from (0,0) and wants to drop an egg bomb vertically
    # The egg bomb drops vertically from the bird's position at some x in [0,X],
    # then falls straight down. The egg bomb must hit (X,Y) without:
    #  - bird hitting obstacles before dropping the egg bomb
    #  - egg bomb hitting obstacles on way down
    #
    # So must find angle and drop point x_drop s.t.:
    #  1) Bird can reach x_drop without obstacle collision
    #  2) Egg bomb dropped at (x_drop, y_drop) falls vertically and hits pig at (X,Y)
    #     This means x_drop == X (egg drops straight down from (X,y_drop))
    #     Egg bomb falls down from y_drop >= Y without intersecting obstacles (no obstacle between y_drop and Y at x=X)
    #
    # So the egg bomb can only be dropped at x = X.
    # So bird must reach (X,y_bird) without hitting obstacles and drop egg bomb down to Y.
    # Check all possible angles to reach (X,y) with y ≥ Y 
    # Because if y < Y egg cannot fall to pig.
    #
    # For given V and X and angle, y = V*sin(angle)*t - 0.5*g*t^2, t = X/(V*cos(angle))
    # So y = X*tan(angle) - g*X^2/(2*V^2*cos(angle)^2)
    #
    # We try angles from a small epsilon to almost pi/2, check if bird can reach (X,y) >= Y without hitting obstacles,
    # and egg bomb can fall down from y to Y without hitting obstacles.
    #
    # If yes print Yes else No.

    if V == 0:
        return False

    for deg in range(1, 900):  # angle 0.01 to 9 rad covers full range
        angle = deg / 100.0
        cos_a = math.cos(angle)
        if cos_a == 0:
            continue
        t = X / (V * cos_a)
        y = V * math.sin(angle) * t - 0.5 * g * t*t
        if y < Y:
            continue
        # Check bird trajectory collision before x = X
        if collides_with_obstacle_trajectory(V, angle, obstacles, X):
            continue
        # Check egg bomb vertical fall from y to Y at x=X
        # Egg bomb path: (X, y') y' in [Y,y]
        # Check if any obstacle covers (X,y') with y' in [Y,y]

        obstruct = False
        for (L,B,R,T) in obstacles:
            if L <= X <= R:
                # Check if obstacle overlaps [Y,y]
                low = min(y, Y)
                high = max(y, Y)
                if T >= low and B <= high:
                    obstruct = True
                    break
        if obstruct:
            continue
        return True
    return False

def main():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    V = int(input_data[1])
    X = int(input_data[2])
    Y = int(input_data[3])
    obstacles = []
    idx = 4
    for _ in range(N):
        L = int(input_data[idx]); B = int(input_data[idx+1]); R = int(input_data[idx+2]); T = int(input_data[idx+3])
        idx += 4
        obstacles.append((L,B,R,T))
    if can_reach_pig(V, X, Y, obstacles):
        print("Yes")
    else:
        print("No")

main()