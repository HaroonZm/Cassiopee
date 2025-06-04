import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 文字フォントを0-12で対応: 0-9,+,-,・
# 7x5の文字ビット表現 (縦7行x横5列)
font = {
    '0': [" ### ","#   #","#  ##","# # #","##  #","#   #"," ### "],
    '1': ["  #  "," ##  ","  #  ","  #  ","  #  ","  #  "," ### "],
    '2': [" ### ","#   #","    #","   # ","  #  "," #   ","#####"],
    '3': [" ### ","#   #","    #","  ## ","    #","#   #"," ### "],
    '4': ["   # ","  ## "," # # ","#  # ","#####","   # ","   # "],
    '5': ["#####","#    ","#### ","    #","    #","#   #"," ### "],
    '6': [" ### ","#   #","#    ","#### ","#   #","#   #"," ### "],
    '7': ["#####","    #","   # ","  #  "," #   "," #   "," #   "],
    '8': [" ### ","#   #","#   #"," ### ","#   #","#   #"," ### "],
    '9': [" ### ","#   #","#   #"," ####","    #","#   #"," ### "],
    '+': ["     ","  #  ","  #  ","#####","  #  ","  #  ","     "],
    '-': ["     ","     ","     ","#####","     ","     ","     "],
    '・':["     ","  #  ","     ","     ","     ","  #  ","     "],
}

# 画像から文字と認識するために7x5の領域を探す
# 盤面は最大201x201なので全探索して文字領域を認識
# 文字同士の重なりなし（隣接は辺でのみ）

N = int(input())
black = set()
min_x = 201
max_x = 0
min_y = 201
max_y = 0

for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        # 縦線
        for y in range(min(y1,y2),max(y1,y2)+1):
            black.add((x1,y))
            if x1 < min_x: min_x = x1
            if x1 > max_x: max_x = x1
            if y < min_y: min_y = y
            if y > max_y: max_y = y
    else:
        # 横線
        for x in range(min(x1,x2),max(x1,x2)+1):
            black.add((x,y1))
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y1 < min_y: min_y = y1
            if y1 > max_y: max_y = y1

# blackマスだけの矩形切り出し
W = max_x - min_x + 1
H = max_y - min_y + 1
canvas = [[0]*W for _ in range(H)]
for (x,y) in black:
    canvas[y - min_y][x - min_x] = 1

# 文字は独立しているので、まずは黒マスの塊(連結成分)抽出
visited = [[False]*W for _ in range(H)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
chars_parts = []

def bfs(sy,sx):
    from collections import deque
    q=deque()
    q.append((sy,sx))
    visited[sy][sx]=True
    pixels=[]
    while q:
        y,x = q.popleft()
        pixels.append((y,x))
        for dy,dx in dirs:
            ny,nx = y+dy,x+dx
            if 0<=ny<H and 0<=nx<W and canvas[ny][nx]==1 and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny,nx))
    return pixels

for y in range(H):
    for x in range(W):
        if canvas[y][x]==1 and not visited[y][x]:
            pixels = bfs(y,x)
            chars_parts.append(pixels)

# chars_partsの各塊の最小矩形作成と7x5にリサイズするために拡大縮小処理
# 文字のレイアウトは7x5ピクセルのパターンなので合わせる
# 連結成分は分離しているが、ある文字の中に別の文字の連結成分が内包される可能性がある
# そのため、このままだと文字が分割されでしまう可能性がある
# したがって1) BFS連結成分をさらにX方向に近い集合に分類して文字単位に統合する必要がある
# ここではまず塊の幅の最小値と最大値を集めて、横方向の連結でマージする

chars_parts.sort(key=lambda ps: min(p[1] for p in ps)) # Xの最小値でソート

merged = []
used = [False]*len(chars_parts)

def overlap(a,b):
    # a,bは塊の座標リスト
    # y,xの最大最小幅
    a_xmin = min(p[1] for p in a)
    a_xmax = max(p[1] for p in a)
    b_xmin = min(p[1] for p in b)
    b_xmax = max(p[1] for p in b)
    # 横領域が接するか近いかでマージ対象とする
    # マスの隣接なしなので共有辺はないが同じ文字は複数線分なので隙間は0～1程度
    # 少しゆるめに1列以内の空きは許す
    return not (a_xmax < b_xmin -1 or b_xmax < a_xmin -1)

def merge_parts(parts_list):
    # 与えられたパーツのリストを横方向のつながりでマージ
    merged_parts = []
    used_sub = [False]*len(parts_list)
    for i in range(len(parts_list)):
        if used_sub[i]:
            continue
        queue = [i]
        merged_pixels = set(parts_list[i])
        used_sub[i]=True
        while queue:
            cid=queue.pop()
            for j in range(len(parts_list)):
                if not used_sub[j]:
                    if overlap(parts_list[cid],parts_list[j]):
                        merged_pixels.update(parts_list[j])
                        used_sub[j]=True
                        queue.append(j)
        merged_parts.append(list(merged_pixels))
    return merged_parts

# 複数回マージして安定させる
tmp = chars_parts
while True:
    nm = merge_parts(tmp)
    if len(nm)==len(tmp):
        break
    tmp=nm
chars_parts = tmp

# chars_partsから文字領域を取り、7x5パターンにリサイズしfont辞書と比較して文字認識
def normalize_pattern(pixels):
    ys = [p[0] for p in pixels]
    xs = [p[1] for p in pixels]
    ymin,ymax = min(ys),max(ys)
    xmin,xmax = min(xs),max(xs)
    h = ymax - ymin + 1
    w = xmax - xmin + 1
    # 7x5にリサイズ
    out = [[0]*5 for _ in range(7)]
    # 元座標→7x5座標への写像
    for y,x in pixels:
        ny = (y - ymin)*7//h
        nx = (x - xmin)*5//w
        if ny>=7: ny=6
        if nx>=5: nx=4
        out[ny][nx] = 1
    return [''.join('#' if c else ' ' for c in row) for row in out]

# font辞書と比較して認識
def match_char(pat):
    for k,v in font.items():
        if all(pat[i]==v[i] for i in range(7)):
            return k
    return '?'

chars = []
for pix in chars_parts:
    p = normalize_pattern(pix)
    c = match_char(p)
    # 文字のX座標（最左端）で並べ替えるため保存
    minx = min(p[1] for p in pix) + min_x
    chars.append((minx,c))

chars.sort(key=lambda x:x[0])
expr = ''.join(c for _,c in chars)

# exprは数字と+-・で構成された文字列
# 先頭の符号も許される

# 演算子優先順位のパース
# ・（乗算）が +,-より優先 (0 < +,- < *)
# ・記号のASCIIでは2バイト文字なので置換して評価しやすくする
expr = expr.replace('・','*').replace('＋','+')

# evalを使わず自前で優先順位つきパース＆計算する（制限でeval禁止想定）

def parse_expression(s):
    # トークン化
    tokens = []
    i=0
    while i < len(s):
        if s[i] in '+-*':
            tokens.append(s[i])
            i+=1
        else:
            j=i
            if s[i] == '-' and (i==0 or s[i-1] in '+-*'):
                # 負の数の認識
                j+=1
                while j < len(s) and s[j].isdigit(): j+=1
                tokens.append(s[i:j])
                i=j
            else:
                while j<len(s) and s[j].isdigit(): j+=1
                tokens.append(s[i:j])
                i=j
    return tokens

tokens = parse_expression(expr)

def calc_expression(tokens):
    # 乗算優先なので
    # 1) 乗算を先に計算し、トークンリストを簡略化
    # 2) 足し算引き算を左から計算
    stack = []
    i=0
    while i < len(tokens):
        t = tokens[i]
        if t == '*':
            prev = stack.pop()
            nxt = tokens[i+1]
            val = int(prev)*int(nxt)
            stack.append(str(val))
            i+=2
        else:
            stack.append(t)
            i+=1

    res = int(stack[0])
    i=1
    while i < len(stack):
        op = stack[i]
        num = int(stack[i+1])
        if op=='+':
            res += num
        else:
            res -= num
        i+=2
    return res

print(calc_expression(tokens))