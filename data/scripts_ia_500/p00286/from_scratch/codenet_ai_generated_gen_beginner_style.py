# 解法の方針
# - 各部品は縦棒N本の間の接続を表す。これは、部品の「あみだくじ」の横棒情報から下側に進むときの番号の移動を示す写像を作ることができる。
# - 1本の部品パーツは1からNまでの並びを変換する写像（長さNの配列）として表現。
# - "+"は写像の合成（適用の連続）、"(m)"は写像の繰り返し（冪乗）。
# - 式全体をパースして、各部品の写像を合成・繰り返しして結果の写像を得る。
# - 最後に1~Nの配列を結果の写像に従って並べ替えて出力する。
#
# - 球面は簡易的にeval禁止で自作パーサ実装（再帰下降パーサ）。
#
# - N<=12なので写像はリストで十分扱いやすい。

import sys
sys.setrecursionlimit(10**7)

N,K=map(int,input().split())
parts={}
for _ in range(K):
    line=input().split()
    name=line[0]
    h=int(line[1])
    grid=[list(map(int,input().split())) for __ in range(h-1)]
    # 部品の変換写像を作る
    # pos: 上端での縦棒番号(1-based)
    # 下端での縦棒はあみだくじのルールに従って追う
    # シミュレーション的に、1~Nをそれぞれ辿って最終位置を求める
    # 高さ方向に順番に横棒での移動をすべて実行
    mapping = list(range(1, N+1))
    for r in range(h-1):
        row = grid[r]
        # 横棒があれば隣の縦棒と番号を交換
        i = 0
        while i < N-1:
            if row[i]==1:
                mapping[i],mapping[i+1]=mapping[i+1],mapping[i]
                i+=1
            i+=1
    parts[name]=mapping

E=int(input())
expressions=[input() for _ in range(E)]

# 式のパーサ
# grammar:
# expr := term { + term }
# term := factor | number(factor)
# factor := partName | '(' expr ')'

s=""
pos=0
def parse_expr():
    global pos
    res=parse_term()
    while pos<len(s) and s[pos]=='+':
        pos+=1
        res2=parse_term()
        res=compose(res,res2)
    return res

def parse_term():
    global pos
    # 数字があるか探す
    start=pos
    while pos<len(s) and s[pos].isdigit():
        pos+=1
    if start!=pos:
        m=int(s[start:pos])
        factor=parse_factor()
        return pow_map(factor,m)
    else:
        return parse_factor()

def parse_factor():
    global pos
    if s[pos] == '(':
        pos+=1
        res = parse_expr()
        if pos>=len(s) or s[pos]!=')':
            # エラー想定外だが無視
            pass
        else:
            pos+=1
        return res
    else:
        # 部品名1文字
        c = s[pos]
        pos+=1
        return parts[c]

def compose(f,g):
    # fとgは長さNのリスト。fを先に適用し、次にgを適用
    # つまり、compose(f,g)[i] = g[f[i]-1]
    return [g[f[i]-1] for i in range(N)]

def pow_map(f,m):
    # 部品の写像のm回繰り返しを計算。繰り返し+高速化は省略し単純実装。mは10^9まで
    # 単純に累乗(冪乗)を繰り返すのは遅いので高速べき乗を実装
    res=list(range(1,N+1))
    base=f
    while m>0:
        if m&1:
            res=compose(res,base)
        base=compose(base,base)
        m>>=1
    return res

for expr in expressions:
    s=expr
    pos=0
    ans=parse_expr()
    print(" ".join(map(str,ans)))