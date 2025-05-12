import numpy as np
import math

N = int(input())

spot = np.zeros(N + 1)
spot[1:] = np.array(list(map(int, input().split())))

tot = int(np.abs(np.roll(spot, 1) - spot).sum())

for i in range(1, N+1):
    print(int(tot - math.fabs(spot[i] - spot[i-1]) - math.fabs(spot[(i+1) % (N+1)] - spot[i])\
            + math.fabs(spot[(i+1) % (N+1)] - spot[i-1])))