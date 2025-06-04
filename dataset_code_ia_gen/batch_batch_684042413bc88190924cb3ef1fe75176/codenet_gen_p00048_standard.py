import sys

classes = [
    (48.00, "light fly"),
    (51.00, "fly"),
    (54.00, "bantam"),
    (57.00, "feather"),
    (60.00, "light"),
    (64.00, "light welter"),
    (69.00, "welter"),
    (75.00, "light middle"),
    (81.00, "middle"),
    (91.00, "light heavy"),
]

for line in sys.stdin:
    w = float(line.strip())
    for limit, rank in classes:
        if w <= limit:
            print(rank)
            break
    else:
        print("heavy")