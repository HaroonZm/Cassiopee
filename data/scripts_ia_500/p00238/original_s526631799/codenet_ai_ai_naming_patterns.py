import sys

def main_loop():
    while True:
        target_value = int(input())
        if target_value == 0:
            sys.exit(0)
        segment_count = int(input())
        segments = [list(map(int, input().split())) for _ in range(segment_count)]
        total_subtracted = sum((segment[1] - segment[0]) for segment in segments)
        result_value = target_value - total_subtracted
        if result_value <= 0:
            print("OK")
        else:
            print(result_value)

if __name__ == "__main__":
    main_loop()