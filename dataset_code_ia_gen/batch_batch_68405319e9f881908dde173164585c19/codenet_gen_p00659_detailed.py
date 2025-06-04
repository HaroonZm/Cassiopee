import sys

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        # 終了条件：n=0
        if n == 0:
            break
        
        # キャラクター名と登場時刻を格納
        character_names = []
        character_times = []
        
        for _ in range(n):
            # 1行に名前とm個の時刻が詰め込まれている形式に対応
            line = input().strip().split()
            name = line[0]
            m = int(line[1])
            times = list(map(int, line[2:2+m]))
            character_names.append(name)
            character_times.append(times)
        
        # 時刻ごとにキャラクター数をカウントするための配列
        # 時刻は0から29まで（制約より）
        time_count = [0]*30
        
        # 各キャラクターの登場時刻をもとにカウント
        for times in character_times:
            for t in times:
                time_count[t] += 1
        
        # 各キャラクターのポイント計算
        # ポイントルール：
        # ある時刻にk人映っていたら、その時刻に映っている各キャラクターは (n - k + 1) ポイントを得る
        # nはケース内のキャラクター数
        points = [0]*n
        for i in range(n):
            for t in character_times[i]:
                k = time_count[t]  # その時刻に映っていた人数
                points[i] += (n - k + 1)
        
        # 最小ポイントのキャラクターを探す
        min_point = min(points)
        
        # 最小ポイントのキャラクターを抽出し，辞書順最小の名前を選ぶ
        candidates = [(character_names[i], points[i]) for i in range(n) if points[i] == min_point]
        candidates.sort(key=lambda x: x[0])
        
        # 出力
        # 最小ポイントと名前
        print(candidates[0][1], candidates[0][0])

if __name__ == "__main__":
    main()