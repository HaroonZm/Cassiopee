from math import hypot
print(f"{hypot(*map(float, input().split()[2:]), *[-i for i in map(float, input().split()[:2])]):.10f}")