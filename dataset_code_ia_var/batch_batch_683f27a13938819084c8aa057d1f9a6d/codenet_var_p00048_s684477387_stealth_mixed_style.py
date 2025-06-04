def classify_weight(w):
    classes = [
        (48.00, "light fly"), (51.00, "fly"), (54.00, "bantam"),
        (57.00, "feather"), (60.00, "light"), (64.00, "light welter"),
        (69.00, "welter"), (75.00, "light middle"), (81.00, "middle"),
        (91.00, "light heavy")
    ]
    for limit, name in classes:
        if w <= limit:
            return name
    return "heavy"

def read_weight():
    from sys import stdin
    for line in stdin:
        try:
            w = float(line.strip())
            print(classify_weight(w))
        except:
            continue

if __name__ == '__main__':
    import sys
    if sys.version_info[0]==3:
        read_weight()
    else:
        while 1:
            try:
                x = float(raw_input())
                print classify_weight(x)
            except:
                break