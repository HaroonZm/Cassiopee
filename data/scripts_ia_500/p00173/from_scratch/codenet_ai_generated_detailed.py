# 入力から各クラスの情報を取得し、総入場者数および収入を計算して出力するプログラム

# 午前の料金は200円、午後の料金は300円で固定
AM_PRICE = 200
PM_PRICE = 300

# 9クラス分のデータを格納するリスト
classes = []

for _ in range(9):
    # 1行でクラス名、午前の入場者数、午後の入場者数を読み込む
    line = input().strip()
    # クラス名と午前・午後の入場者数に分割
    name, am_str, pm_str = line.split()
    am_visitors = int(am_str)
    pm_visitors = int(pm_str)
    
    # 総入場者数の計算
    total_visitors = am_visitors + pm_visitors
    # 収入の計算（午前と午後の入場者数 × 料金）
    income = am_visitors * AM_PRICE + pm_visitors * PM_PRICE
    
    # タプルでリストに保存
    classes.append((name, total_visitors, income))

# 計算結果を出力
for cls in classes:
    print(cls[0], cls[1], cls[2])