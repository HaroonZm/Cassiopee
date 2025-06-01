heights = []
while True:
    try:
        line = input()
        if line == "":
            break
        height = float(line)
        heights.append(height)
    except EOFError:
        break

max_height = max(heights)
min_height = min(heights)
difference = max_height - min_height

print(difference)