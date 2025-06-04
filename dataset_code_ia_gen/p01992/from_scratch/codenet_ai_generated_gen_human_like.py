import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

stack = []
pos = dict()  # 先頭文字 -> インデックス(スタック内の位置)

for w in words:
    c = w[0]
    if c in pos:
        i = pos[c]
        # i以降を全部取り除く
        for _ in range(len(stack) - i):
            removed = stack.pop()
            del pos[removed[0]]
    pos[c] = len(stack)
    stack.append(w)

print(len(stack))