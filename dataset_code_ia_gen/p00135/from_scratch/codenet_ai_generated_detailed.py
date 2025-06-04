# 時計の短針と長針の角度差を計算し、
# 角度差に応じて "alert", "safe", "warning" を出力するプログラム

def calculate_angle(h, m):
    # 短針の角度計算
    # 短針は1時間で30度(360度/12)動き、分によっても動く（1分で0.5度）
    hour_angle = (h % 12) * 30 + m * 0.5
    
    # 長針の角度計算
    # 長針は1分で6度(360度/60)動く
    minute_angle = m * 6
    
    # 2つの針の角度差を計算（0〜180度の範囲に収める）
    angle_diff = abs(hour_angle - minute_angle)
    if angle_diff > 180:
        angle_diff = 360 - angle_diff
        
    return angle_diff

def judge_angle(angle):
    # 近い：0度以上30度未満
    if 0 <= angle < 30:
        return "alert"
    # 遠い：90度以上180度以下
    elif 90 <= angle <= 180:
        return "safe"
    # それ以外
    else:
        return "warning"

def main():
    n = int(input())
    for _ in range(n):
        time_str = input().strip()
        hh, mm = map(int, time_str.split(":"))
        
        angle = calculate_angle(hh, mm)
        result = judge_angle(angle)
        print(result)

if __name__ == "__main__":
    main()