import sys
import bisect

limits = [48, 51, 54, 57, 60, 64, 69, 75, 81, 91]
classes = ['light fly', 'fly', 'bantam', 'feather', 'light', 'light welter', 'welter', 'light middle', 'middle', 'light heavy', 'heavy']

for line in sys.stdin:
    try:
        w = float(line)
        idx = bisect.bisect_right(limits, w)
        print(classes[idx])
    except ValueError:
        break