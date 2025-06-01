N, *times_N = map(int, input().split())
M, *times_M = map(int, input().split())

bus_times = set()
for i in range(N):
    h = times_N[2*i]
    m = times_N[2*i+1]
    bus_times.add((h, m))
for i in range(M):
    h = times_M[2*i]
    m = times_M[2*i+1]
    bus_times.add((h, m))

bus_times = sorted(bus_times)

output = []
for h, m in bus_times:
    output.append(f"{h}:{m:02d}")
print(" ".join(output))