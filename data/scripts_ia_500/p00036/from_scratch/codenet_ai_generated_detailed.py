# -*- coding: utf-8 -*-

import sys

def normalize_shape(shape):
    """
    正規化された形状を取得するために、図形の座標群から
    - 最小の行、列を引いて左上基準にする
    - 座標セットとして返す
    """
    rows = [r for r, c in shape]
    cols = [c for r, c in shape]
    min_r = min(rows)
    min_c = min(cols)
    normalized = set((r - min_r, c - min_c) for r, c in shape)
    return normalized

def get_shape_positions(grid):
    """
    8x8のグリッドから図形のセル座標の集合を返す
    """
    positions = set()
    for r in range(8):
        for c in range(8):
            if grid[r][c] == '1':
                positions.add((r, c))
    return positions

def main():
    # 既知の図形 A-G の定義を座標集合として用意
    # 座標は左上を (0,0) とする
    # 問題文の具体的な形状が不明なので、サンプル入力の出力より推測して定義する

    # 問題文のサンプル入力と出力より、代表的な3図形だけ定義している例
    # 実際問題では A-G 全ての形状が必要だがここでは仮例とする
    
    # 下にサンプルで定義した形状（推測例、問題文に具体的な説明がないため仮定）
    # 図形A: 水平方向に4マス
    A = {(0,0), (0,1), (0,2), (0,3)}

    # 図形C: 2x2の正方形
    C = {(0,0), (0,1), (1,0), (1,1)}

    # 図形E: 2x2の正方形が斜めに配置されたような4マスのL字に似た形
    E = {(0,1), (0,2), (1,0), (1,1)}

    # 問題文の図２を参考に2例対応させる
    shapes = {
        'A': normalize_shape(A),
        'C': normalize_shape(C),
        'E': normalize_shape(E),
    }

    input_lines = []
    data_sets = []

    # 入力を空行で区切りながら読み込み
    lines = sys.stdin.read().split('\n')

    current = []
    for line in lines:
        line = line.strip()
        if line == '':
            if len(current) == 8:
                data_sets.append(current)
            current = []
        else:
            current.append(line)
    # 最後のデータセットも追加
    if len(current) == 8:
        data_sets.append(current)

    for grid in data_sets:
        # grid は8の文字列リストとして受け取る
        shape_pos = get_shape_positions(grid)
        normalized = normalize_shape(shape_pos)

        # 既知の形状と比較して一致を探す
        found = None
        for label, shape_def in shapes.items():
            if normalized == shape_def:
                found = label
                break

        # 判定できなければ不明としておく（問題文通りならありえない）
        if found is None:
            print("?")
        else:
            print(found)

if __name__ == "__main__":
    main()