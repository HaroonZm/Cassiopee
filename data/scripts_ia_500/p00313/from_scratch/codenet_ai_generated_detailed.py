# Pythonプログラム: 問題の集合演算に基づく条件を満たす人物の数を計算する

# 入力例：
# N = 人数
# 次の行でAの人数XとそのメンバーID
# 次の行でBの人数YとそのメンバーID
# 次の行でCの人数ZとそのメンバーID
#
# 条件： (Aの補集合 ∩ C) ∪ (B ∩ C)
# すなわち、Aに属さないかつCに属する者 OR Bに属しかつCに属する者の個数を求める

def main():
    # 調査対象の人数を取得
    N = int(input())
    
    # Aに属する者の情報を取得
    A_data = list(map(int, input().split()))
    X = A_data[0]  # Aに属する人数
    A = set(A_data[1:])  # Aのメンバー集合
    
    # Bに属する者の情報を取得
    B_data = list(map(int, input().split()))
    Y = B_data[0]  # Bに属する人数
    B = set(B_data[1:])  # Bのメンバー集合
    
    # Cを所持する者の情報を取得
    C_data = list(map(int, input().split()))
    Z = C_data[0]  # Cを所持する人数
    C = set(C_data[1:])  # Cを所持する者集合
    
    # 全体集合を1からNまでのセットで作成
    all_people = set(range(1, N+1))
    
    # Aの補集合: Aに属さない者の集合
    not_A = all_people - A
    
    # 条件に該当する集合を計算
    # (not_A ∩ C) ∪ (B ∩ C)
    condition_set = (not_A & C) | (B & C)
    
    # 条件に合致する人数を出力
    print(len(condition_set))

if __name__ == "__main__":
    main()