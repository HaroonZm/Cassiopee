n = int(input())
import math
for i in range(1, 46298):
    if math.floor(i * 1.08) == n:
        print(i)
        break
else:
    print(":(")