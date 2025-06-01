import sys

# 入力の巡回記録から列車の編成を復元する関数
def reconstruct_train(record):
    # recordは「a->b<-a<-c」のような文字列
    # 車両記号と移動方向で区切られている
    # 入力例：a->e->c->b->d
    # 解析のために、文字列を車両記号と方向の交互列に分割する
    
    # まず先頭の車両を取り出す
    # 以降、(方向, 車両) ペアが続く
    
    # 例: "a->e->c->b->d" -> ['a', '->', 'e', '->', 'c', '->', 'b', '->', 'd']
    tokens = []
    i = 0
    while i < len(record):
        c = record[i]
        if c.isalpha():
            tokens.append(c)
            i += 1
        else:
            # 方向記号
            if i + 1 < len(record):
                tokens.append(record[i:i+2])
                i += 2
            else:
                # 入力の形式上、ここに来ることはないはず
                i += 1

    # tokensは交互に [車両, 方向, 車両, 方向, ...]の繰り返しでない。実際は、先頭車両 [車両], 次に [方向, 車両], [方向, 車両]...
    # 例えば: ['a', '->', 'e', '->', 'c', '->', 'b', '->', 'd']
    # tokens[0] が初めの車両、以降は (方向, 車両) のペアで続く
    
    # 隣接関係を管理するために辞書を使う
    # key: 車両記号, value: (前方の車両, 後方の車両)
    # 最初はNoneで初期化
    neighbors = {}
    
    def ensure_car(car):
        if car not in neighbors:
            neighbors[car] = [None, None]  # [front, back]
    
    # 初めの車両を確保
    current = tokens[0]
    ensure_car(current)
    
    # tokens の (方向, 車両) を順に解析し、関係を辿る
    i = 1
    while i < len(tokens):
        direction = tokens[i]       # '->' または '<-'
        next_car = tokens[i+1]
        ensure_car(next_car)
        
        # currentからnext_carへの移動方向は direction
        # direction が '->' の場合、次の車両は current の後方
        # direction が '<-' の場合、次の車両は current の前方
        if direction == '->':
            # current の後ろに next_car がある
            # 隣接関係をセット
            # current.back = next_car
            # next_car.front = current
            # 既に登録されていたら、一致するか検証する
            
            # currentの後方が未登録なら登録、異なるなら不整合（問題文では不整合想定不要と推定）
            if neighbors[current][1] is None:
                neighbors[current][1] = next_car
            elif neighbors[current][1] != next_car:
                # 矛盾？（ここでは無視）
                pass
            
            # next_carの前方も同様に登録
            if neighbors[next_car][0] is None:
                neighbors[next_car][0] = current
            elif neighbors[next_car][0] != current:
                pass
            
        else:  # direction == '<-'
            # current の前に next_car がある
            # current.front = next_car
            # next_car.back = current
            if neighbors[current][0] is None:
                neighbors[current][0] = next_car
            elif neighbors[current][0] != next_car:
                pass
            
            if neighbors[next_car][1] is None:
                neighbors[next_car][1] = current
            elif neighbors[next_car][1] != current:
                pass
        
        # currentをnext_carに更新（巡回記録の移動先へ進む）
        current = next_car
        i += 2
    
    # 隣接辞書 neighbors が完成
    # 列車は線形リストで、先頭車両は "前方(None)" がない車両
    # 先頭車両を探す
    start_candidates = [car for car in neighbors if neighbors[car][0] is None]
    # １つとは限らないかもしれないが、本問題では1つと考える
    start = start_candidates[0]
    
    # 先頭から後方に繋げて列車の編成を復元する
    result = []
    current = start
    while current is not None:
        result.append(current)
        current = neighbors[current][1]
    
    return ''.join(result)


def main():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        s = input().rstrip('\n')
        ans = reconstruct_train(s)
        print(ans)

if __name__ == "__main__":
    main()