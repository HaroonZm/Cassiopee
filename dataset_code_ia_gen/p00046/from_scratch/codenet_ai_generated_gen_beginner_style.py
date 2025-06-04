import sys

heights = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    heights.append(float(line))

max_height = max(heights)
min_height = min(heights)

diff = max_height - min_height
print(diff)