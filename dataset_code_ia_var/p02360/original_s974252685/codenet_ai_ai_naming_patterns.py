import sys
from itertools import accumulate

def main():
    input_rect_count = int(input())

    y_sweep_marks = [0] * 1001
    rectangle_events = [None] * (2 * input_rect_count)
    event_idx = 0

    for input_line in sys.stdin:
        rect_x1, rect_y1, rect_x2, rect_y2 = [int(coord) for coord in input_line.split()]
        rectangle_events[event_idx] = (rect_x2, -1, rect_y1, rect_y2)
        rectangle_events[event_idx + input_rect_count] = (rect_x1, 1, rect_y1, rect_y2)
        event_idx += 1

    rectangle_events.sort(key=lambda event: event[0])

    current_max_overlap = 0

    for event_x, event_type, event_y1, event_y2 in rectangle_events:
        if event_type > 0:
            y_sweep_marks[event_y1] += 1
            y_sweep_marks[event_y2] -= 1
        else:
            event_overlap = max(accumulate(y_sweep_marks))
            if event_overlap > current_max_overlap:
                current_max_overlap = event_overlap
            y_sweep_marks[event_y1] -= 1
            y_sweep_marks[event_y2] += 1

    print(current_max_overlap)

if __name__ == "__main__":
    main()