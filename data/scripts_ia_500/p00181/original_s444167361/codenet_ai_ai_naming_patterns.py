import sys
from sys import stdin
input = stdin.readline

def can_divide_books_into_segments(segments_count, books_count, max_segment_width, books_widths):
    if max(books_widths) > max_segment_width:
        return False

    remaining_width = max_segment_width
    remaining_segments = segments_count
    books_queue = books_widths[:]

    while books_queue:
        while books_queue and remaining_width >= books_queue[0]:
            remaining_width -= books_queue[0]
            books_queue = books_queue[1:]
            if not books_queue:
                break
        remaining_width = max_segment_width
        remaining_segments -= 1

    return remaining_segments >= 0

def find_minimum_max_segment_width(segments_count, books_count, books_widths):
    upper_bound = 1500000
    lower_bound = 0
    minimum_max_width = float('inf')

    for _ in range(100):
        mid_width = (upper_bound + lower_bound) // 2
        if can_divide_books_into_segments(segments_count, books_count, mid_width, books_widths):
            minimum_max_width = min(minimum_max_width, mid_width)
            upper_bound = mid_width
        else:
            lower_bound = mid_width

    return minimum_max_width

def main(args):
    while True:
        segments_count, books_count = map(int, input().split())
        if segments_count == 0 and books_count == 0:
            break
        books_widths = [int(input()) for _ in range(books_count)]
        result = find_minimum_max_segment_width(segments_count, books_count, books_widths)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])