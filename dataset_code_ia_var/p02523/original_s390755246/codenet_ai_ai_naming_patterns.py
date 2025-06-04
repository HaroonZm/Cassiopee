import math
coordinate_x1, coordinate_x2, coordinate_y1, coordinate_y2 = map(float, raw_input().split())
delta_x = coordinate_y1 - coordinate_x1
delta_y = coordinate_y2 - coordinate_x2
distance = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))
print distance