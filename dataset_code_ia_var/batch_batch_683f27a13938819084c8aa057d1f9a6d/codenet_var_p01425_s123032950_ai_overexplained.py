import sys  # Import the sys module to access system-specific parameters and functions
input = sys.stdin.readline  # Assign sys.stdin.readline (faster input reading) to variable 'input'

# Function to compute the vertical position (y) of a projectile after time 't'
def calc_y(vy, t):
    # vy is the initial vertical velocity
    # t is the time elapsed
    # The formula used is y = vy*t - (g/2)*t^2, which comes from the equations of uniformly accelerated motion
    # g is the acceleration due to gravity
    return vy * t - g / 2 * t * t

# Function to determine the location of a point 'y' relative to an interval [b, t] (bottom, top)
def loc(y, b, t):
    # y is the height to check
    # b is the bottom bound of the obstacle
    # t is the top bound of the obstacle
    # eps is a small epsilon (tiny positive number) to account for possible floating point inaccuracies
    if y < b + eps:
        # If y is below the bottom (considering epsilon), return -1 (below)
        return -1
    if y > t - eps:
        # If y is above the top (considering epsilon), return 1 (above)
        return 1
    # Otherwise, y is within [b, t], so return 0 (inside)
    return 0

# Function to check if a projectile can hit a specific target (x, y)
def can_hit(x, y):
    # x is the horizontal distance to the target
    # y is the vertical distance to the target
    # The function checks if it's physically possible to reach (x, y) and if any obstacles block the path

    if x == 0:
        # If the target is in the exact same vertical line as the origin, return False,
        # since only vertical shooting remains and is separately handled in the main logic
        return False

    # Calculate coefficients for the quadratic equation in t^2 describing possible flight trajectories
    # Derived from the physics equations:
    # a*t^4 + b*t^2 + c = 0, for the range equations solved for t
    a = g * g / 4  # Quadratic coefficient
    b = g * y - V * V  # Linear coefficient
    c = x * x + y * y  # Constant term

    # Compute the discriminant (D) to check if real solutions (i.e., feasible launch angles/speeds) exist
    D = b * b - 4 * a * c

    if D < -eps:
        # If the discriminant is negative (even after allowing for small errors), no real solution exists
        # (i.e., the point is physically unreachable with current speed)
        return False

    if -eps <= D < 0:
        # If D is close to zero but not negative, set D = 0 for numerical stability
        D = 0

    # Try both roots given by quadratic formula; these correspond to possible launch angles
    for d in [-1, 1]:
        # d picks each solution (adding and subtracting the square root)
        t2 = (-b + d * D ** 0.5) / (2 * a)  # this is t^2; must be positive
        if t2 <= 0:
            # If t^2 is not positive, skip (no physical solution)
            continue
        t = t2 ** 0.5  # take the square root to get time of flight

        vx = x / t  # The initial horizontal velocity is distance divided by time
        vy = y / t + g / 2 * t  # The initial vertical velocity derived from motion equations

        # Check if the projectile, after firing with these parameters, ever goes over the target
        # by plugging back into equations at the horizontal location X (where the pig is)
        if calc_y(vy, X / vx) < Y - eps:
            # If at the pig's position (X), the height is below the pig's height (Y), skip
            continue

        # Compute the max height along the trajectory
        maxt = vy / g  # Time to reach peak (when vertical speed becomes zero)
        maxx = vx * maxt  # Horizontal distance at peak
        maxy = calc_y(vy, maxt)  # Maximum height reached

        # Now, for each obstacle on the field, check if the trajectory intersects it
        for L, B, R, T in obstacles:
            # For each vertical edge of the obstacle (left L, right R), check projectile y-coordinates
            left = loc(calc_y(vy, L / vx), B, T)   # Where is projectile at left edge (relative to obstacle bounds)
            right = loc(calc_y(vy, R / vx), B, T)  # Same for right edge

            if left * right <= 0:
                # If left and right locations have different signs or either is zero,
                # the projectile crosses or grazes the obstacle; thus, path is blocked
                break

            # Check if the max point (apex) of the trajectory is horizontally within the obstacle
            if L <= maxx <= R:
                mid = loc(maxy, B, T)
                if left * mid <= 0:
                    # If the apex passes through the obstacle, path is also blocked
                    break
        else:
            # If no obstacle breaks the path, then hitting the pig is possible
            return True

    # After checking all possible flight paths and obstacles, if none succeed, return False
    return False

g = 9.8  # Gravitational acceleration (meters per second squared)
eps = 1e-10  # Epsilon for floating point comparison

# Read integers from input:
# N: number of obstacles
# V: initial speed of projectile
# X: horizontal distance to the pig
# Y: vertical distance to the pig
N, V, X, Y = map(int, input().split())

# List to store obstacles. Each obstacle is represented by its rectangle:
# (L: left, B: bottom, R: right, T: top)
obstacles = []
for _ in range(N):
    L, B, R, T = map(int, input().split())  # Read each obstacle's boundaries

    R = min(R, X)  # Cap the right-side of the obstacle so it doesn't go past the pig's x-position

    if L <= X:
        # Only consider obstacles that are before or at the position of the pig
        obstacles.append((L, B, R, T))

if X == 0:
    # Special case: the pig is directly above the starting point

    # The maximal height the projectile can reach is (V^2)/(2*g) (classic physics)
    if V * V / (2 * g) < Y - eps:
        # If even the maximum possible y is below the pig, can't hit it
        print('No')
        exit()
    # Now check for obstacles in the vertical path
    for L, B, R, T in obstacles:
        if B < Y:
            # If any obstacle extends below the pig's height, it's blocking the path vertically
            print('No')
            exit()
    # If no obstacles block the vertical path and pig is within reach, the answer is yes
    print('Yes')
    exit()

# Try to hit the pig directly by checking if there's an available flight path
if can_hit(X, Y):
    print('Yes')
    exit()

# If direct hit is not possible, try to hit the top corners of each obstacle in case pig can be hit after rebound
for L, B, R, T in obstacles:
    # Try hitting either left or right top corners of the obstacle
    if can_hit(L, T) or can_hit(R, T):
        print('Yes')
        exit()

# If no solution found after all checks, print 'No'
print('No')