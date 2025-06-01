import sys
import bisect

def main():
    input = sys.stdin.readline
    
    while True:
        d = int(input())
        if d == 0:
            break
        
        n = int(input())
        m = int(input())
        
        # 本店S1は位置0に固定
        # 他の店舗の位置を読み込み、昇順にソートする
        stores = [0]  # 本店の位置
        for _ in range(n - 1):
            pos = int(input())
            stores.append(pos)
        stores.sort()
        
        # 環状線上の点kに対し、各店舗までの距離は時計回りおよび反時計回りの最短距離
        # 店舗の位置は昇順にソートされているので、二分探索でkが入る位置付近の店舗を探し、
        # そこから距離の最小値を求める
        
        total_distance = 0
        for _ in range(m):
            k = int(input())
            # kの位置を探す（storesはソート済み）
            idx = bisect.bisect_left(stores, k)
            
            candidates = []
            # idx にある店舗（もしidxがnならば範囲外）
            if idx < n:
                # 時計回りおよび反時計回りの距離を考慮し最短距離を計算
                dist = abs(stores[idx] - k)
                candidates.append(min(dist, d - dist))
            # idx - 1 の店舗も候補
            if idx > 0:
                dist = abs(stores[idx - 1] - k)
                candidates.append(min(dist, d - dist))
            
            total_distance += min(candidates)
        
        print(total_distance)

if __name__ == "__main__":
    main()