import sys
import math

for line in sys.stdin:
    if line.strip() == '':
        continue
    N_D = line.strip().split()
    if len(N_D) != 2:
        continue
    N, D = map(int, N_D)
    if N == 0 and D == 0:
        break
    instructions = []
    for _ in range(N):
        Ls, Rs, t = map(int, sys.stdin.readline().strip().split())
        instructions.append((Ls, Rs, t))
    
    # initial position and orientation
    x, y = 0.0, 0.0
    theta = 0.0  # angle in radians, 0 means facing along positive x-axis
    
    # Convert degrees to radians helper
    def deg2rad(deg):
        return deg * math.pi / 180.0
    
    # For each instruction:
    for Lspeed, Rspeed, t in instructions:
        # Calculate linear velocities of wheels
        # Distance each wheel travels = radius * wheel rotation in radians
        # wheel_radius = 1
        left_dist = deg2rad(Lspeed) * t
        right_dist = deg2rad(Rspeed) * t
        # linear velocity of left and right wheels
        v_l = left_dist / t
        v_r = right_dist / t
        
        # Linear and angular velocity of buggy
        v = (v_r + v_l) / 2.0
        omega = (v_r - v_l) / (2.0 * D)
        
        if abs(omega) < 1e-15:
            # Moving straight
            dx = v * t * math.cos(theta)
            dy = v * t * math.sin(theta)
            x += dx
            y += dy
            # orientation unchanged
        else:
            # Moving along a circle of radius R = v / omega
            R = v / omega
            # center of rotation coordinates (xc, yc)
            xc = x - R * math.sin(theta)
            yc = y + R * math.cos(theta)
            # update angle
            theta_new = theta + omega * t
            
            # new position of buggy
            x = xc + R * math.sin(theta_new)
            y = yc - R * math.cos(theta_new)
            theta = theta_new
    
    print(f"{x:.5f}")
    print(f"{y:.5f}")