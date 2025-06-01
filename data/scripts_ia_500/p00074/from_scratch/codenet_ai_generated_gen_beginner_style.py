while True:
    T, H, S = map(int, input().split())
    if T == -1 and H == -1 and S == -1:
        break
    total_seconds = 120 * 60
    elapsed_seconds = T * 3600 + H * 60 + S
    remain_std = total_seconds - elapsed_seconds
    remain_3x = remain_std * 3

    # standard mode
    h_std = remain_std // 3600
    m_std = (remain_std % 3600) // 60
    s_std = remain_std % 60

    # 3x mode
    h_3x = remain_3x // 3600
    m_3x = (remain_3x % 3600) // 60
    s_3x = remain_3x % 60

    print(f"{h_std:02d}:{m_std:02d}:{s_std:02d}")
    print(f"{h_3x:02d}:{m_3x:02d}:{s_3x:02d}")