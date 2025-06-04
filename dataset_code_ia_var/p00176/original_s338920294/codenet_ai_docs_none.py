import math
while True:
    color = [[0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255], [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255]]
    color_16 = input()
    if color_16 == "0":
        break
    color_R = int(color_16[1] + color_16[2], 16)
    color_G = int(color_16[3] + color_16[4], 16)
    color_B = int(color_16[5] + color_16[6], 16)
    min_d = 500
    for i in range(8):
        R = color[i][0]
        G = color[i][1]
        B = color[i][2]
        d = math.sqrt((R - color_R)**2 + (G - color_G)**2 + (B - color_B)**2)
        if min_d > d:
            min_d = d
            color_num = i
    if color_num == 0:
        print("black")
    elif color_num == 1:
        print("blue")
    elif color_num == 2:
        print("lime")
    elif color_num == 3:
        print("aqua")
    elif color_num == 4:
        print("red")
    elif color_num == 5:
        print("fuchsia")
    elif color_num == 6:
        print("yellow")
    else:
        print("white")