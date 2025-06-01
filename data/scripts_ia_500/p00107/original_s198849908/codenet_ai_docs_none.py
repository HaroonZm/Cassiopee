import math

output = []

while True:
    depth, width, height = map(int, input().split())

    if depth == 0 and width == 0 and height == 0:
        break

    cheeseRadius = math.sqrt((width / 2)**2 + (height / 2)**2)

    inputCount = int(input())

    for _ in range(inputCount):
        entranceRadius = int(input())

        if cheeseRadius < entranceRadius:
            output.append("OK")
        else:
            output.append("NA")

print("\n".join(output))