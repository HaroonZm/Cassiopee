import sys
sys.setrecursionlimit(10**7)

def shiritori_compression(words):
    # スタックを用いて単語列を圧縮する
    # i < j かつ w_i の先頭文字 == w_j の先頭文字が見つかれば、
    # i以上j-1以下の単語をまとめて削除する（スタックの先頭からj-1まで取り除くイメージ）
    stack = []
    for w in words:
        first_char = w[0]
        # スタックの最後の単語の先頭文字 == 今の単語の先頭文字ならば
        # 冗長な部分列発見 -> その部分列を削除する
        # iはスタックの中の同じ先頭文字だった単語の位置
        # 「今の単語」をスタックに加えるのは、削除後の末尾になる可能性があるため
        while stack and stack[-1][0] == first_char:
            # ここで、スタックの最後の先頭文字と今の単語の先頭文字が同じなので
            # i = index of the first occurrence of that character in stack from the end possible,
            # but stack has only unique first characters preserved due to the removals,
            # so we simply pop the word at the end, effectively removing intermediate words.
            # Actually, problem states removing i through j-1, keeping w_j,
            # our stack stores words after removals, so popping top removes the redundant words.
            stack.pop()
        stack.append(w)
    return len(stack)

def main():
    input = sys.stdin.readline
    N = int(input())
    words = [input().rstrip('\n') for _ in range(N)]
    # 問題文の条件から、先頭文字が直前の単語の末尾文字と一致する列であることが保証されており、
    # 同じ単語の繰り返しはないので、上のアルゴリズムで正しく圧縮できる。
    ans = shiritori_compression(words)
    print(ans)

if __name__ == "__main__":
    main()