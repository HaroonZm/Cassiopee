def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    total_recording_seconds = 120 * 60  # 2 hours in seconds
    while True:
        line = input().strip()
        if not line:
            continue
        H, M, S = map(int, line.split())
        if H == -1 and M == -1 and S == -1:
            break
        elapsed = H * 3600 + M * 60 + S
        remain_standard = total_recording_seconds - elapsed
        remain_triple = remain_standard * 3
        print(format_time(remain_standard))
        print(format_time(remain_triple))

if __name__ == "__main__":
    main()