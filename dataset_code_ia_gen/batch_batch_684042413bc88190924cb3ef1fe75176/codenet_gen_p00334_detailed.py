# 入力された三角形の面情報から、頂点番号の組み合わせが同じ面をまとめて、
# 重複している面の数を求める。
# 各面の頂点番号3つをソートしてから集合に格納することで、
# 順序の違いによる同一面の重複を検出する。

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    faces = []
    for _ in range(N):
        p = list(map(int, input().split()))
        # 頂点番号をソートして標準化
        faces.append(tuple(sorted(p)))

    unique_faces = set()
    duplicates = 0

    for f in faces:
        if f in unique_faces:
            # すでにある面なら重複としてカウント
            duplicates += 1
        else:
            unique_faces.add(f)

    print(duplicates)

if __name__ == "__main__":
    main()