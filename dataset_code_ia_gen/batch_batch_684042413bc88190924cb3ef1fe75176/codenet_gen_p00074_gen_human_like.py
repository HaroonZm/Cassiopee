def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

while True:
    H, M, S = map(int, input().split())
    if H == -1 and M == -1 and S == -1:
        break

    elapsed_seconds = H * 3600 + M * 60 + S
    total_seconds = 120 * 60  # 2 hours in seconds

    # remaining time in standard recording mode
    remain_standard = total_seconds - elapsed_seconds

    # remaining time in 3x recording mode
    remain_three_times = remain_standard * 3

    print(format_time(remain_standard))
    print(format_time(remain_three_times))