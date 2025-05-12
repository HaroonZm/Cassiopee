# Your code here!
import math

N, M = map(int, input().split())
if abs(N - M) >= 2:
    print(0)
elif abs(N - M) == 1:
    print(math.factorial(N) * math.factorial(M) % (pow(10, 9) + 7))
else:
    print(math.factorial(N) * math.factorial(M) * 2 % (pow(10, 9) + 7))