import math

# Initial position (x, y) and initial direction in degrees
x, y = 0.0, 0.0
direction = 0.0  # facing east initially (0 degrees)

while True:
    # Read input line, remove spaces, split by comma
    line = input().strip()
    if line == "0,0":
        break
    d_str, t_str = line.split(",")
    d = int(d_str)
    t = int(t_str)

    # Move forward d steps in the current direction
    # Convert direction to radians for math functions
    rad = math.radians(direction)
    # Calculate displacement
    dx = d * math.cos(rad)
    dy = d * math.sin(rad)
    x += dx
    y += dy

    # Turn clockwise by t degrees
    # Since positive angle rotates counterclockwise, clockwise turn means subtract angle
    direction -= t

# Print final coordinates truncated to integer
print(int(x))
print(int(y))