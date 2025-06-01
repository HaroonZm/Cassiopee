import sys
import re

def main():
    n = int(sys.stdin.readline())
    
    # 正規表現のパターン定義
    # A種:
    # >' の後に = が1個以上
    # その後 # が1回
    # そして先頭で数えた = と同じ数だけ = が続き
    # 最後に ~ で終わる
    # ＝の数をキャプチャし、後半も同じ数になるかをグループ反復で確認
    pattern_A = re.compile(r"^>'(=+)(#)(=+)(~)$")
    
    # B種:
    # >^ の後に Q= の繰り返しが1回以上
    # 最後に ~~ で終わる
    # (Q=)+ の繰り返しを確認しそのまま末尾で~~
    pattern_B = re.compile(r"^>\^(Q=)+~~$")
    
    for _ in range(n):
        s = sys.stdin.readline().rstrip('\n')
        
        # A種判定
        m = pattern_A.match(s)
        if m:
            left_eq = m.group(1)
            right_eq = m.group(3)
            # 左側と右側の=の数が同じか確認
            if len(left_eq) == len(right_eq):
                print("A")
                continue
        
        # B種判定
        if pattern_B.match(s):
            print("B")
            continue
        
        # NA判定
        print("NA")

if __name__ == "__main__":
    main()