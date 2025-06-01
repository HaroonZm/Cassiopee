heights = []
while True:
    try:
        h = float(input("Enter a height: "))  # asking user for height
        heights.append(h)
    except Exception:  # when input can't be converted, just stop
        break

difference = max(heights) - min(heights)
print("Difference between max and min is", difference)