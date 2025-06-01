import sys
sys.setrecursionlimit(10**7)

N,K=map(int,input().split())
parts={}
for _ in range(K):
    name,h= input().split()
    h=int(h)
    g=[]
    for __ in range(h-1):
        line = list(map(int,input().split()))
        g.append(line)
    parts[name]=(h,g)

# 部品ごとにその部品が示す置換(permutation)を計算する
# あみだくじのルールにより、上端から番号1..Nがどう対応するか調べる
def get_perm(name):
    h,g=parts[name]
    # posは縦棒番号の位置(1-based)
    # 横棒がある位置で左右に移動する
    res=list(range(N))
    for top in range(N):
        pos=top
        for r in range(h-1):
            # r行目の横棒情報 g[r][c]は縦棒cとc+1の間の横棒(0-based)
            # posが縦棒cなら横棒があればpos+1に横移動、pos=c+1ならpos-1に横移動
            if pos>0 and g[r][pos-1]==1:
                pos-=1
            elif pos<N-1 and g[r][pos]==1:
                pos+=1
        res[top]=pos
    # res[top]はtopから下に辿った結果の位置(0-based)
    # 0-basedを1-based順列に変換
    perm=[0]*N
    for i,v in enumerate(res):
        perm[i]=v
    # perm: i番目の縦棒がi番目の数字をどこに送るか(0-based)
    return perm

# 部品名からpermutationを取り出す
part_perm={}
for p in parts:
    part_perm[p]=get_perm(p)

# 式のパースを行い、結果としてpermutationを返す
# perm: 0-basedで、perm[i]=jならi番目の縦棒の数字がj番目の縦棒へ行く
# permはリスト長Nの整数の順列(0~N-1)の並び

# 式の構文は以下
# expr = term [('+' term)*]
# term = [int '('] expr ')'
#
# 例:
# 2(A+B) -> 2*(A+B)
# 部品はA,B,C...各1文字

# さらに繰り返しは累乗的に適用 (permの合成)を繰り返す
# 直積ではなく合成: f∘g(x) = g(f(x))が正しい?
# あみだくじの合成は左から右に順番に合成
# A+BはAの置換を適用後にBの置換を適用(左から右)
# つまり f(g(x))は先にg,次にfなので引数順に注意
# ここでは順番通りの合成を書く

class Parser:
    def __init__(self,s):
        self.s=s
        self.i=0

    def parse_int(self):
        num=0
        start=self.i
        while self.i<len(self.s) and self.s[self.i].isdigit():
            num=num*10+int(self.s[self.i])
            self.i+=1
        if self.i==start:
            return None
        return num

    def parse_factor(self):
        # factorは部品文字か繰り返し表現
        # 繰り返しは数字に続く括弧つきexpr: m(expr)
        # 部品は1文字の英大文字
        num=self.parse_int()
        if num is not None:
            # 次は(なので必ずかっこあるはず
            assert self.i<len(self.s) and self.s[self.i]=='('
            self.i+=1
            expr=self.parse_expr()
            assert self.i<len(self.s) and self.s[self.i]==')'
            self.i+=1
            return (num, expr)
        else:
            # 部品名か括弧式か
            if self.i<len(self.s) and self.s[self.i]=='(':
                self.i+=1
                expr=self.parse_expr()
                assert self.i<len(self.s) and self.s[self.i]==')'
                self.i+=1
                return (1, expr) # 1回繰り返し
            else:
                # must be part name 1字
                c=self.s[self.i]
                self.i+=1
                if c not in part_perm:
                    raise ValueError("Unknown part name "+c)
                return (1, c)

    def parse_term(self):
        # term: factor '+' term | factor
        num1,f1=self.parse_factor()
        perm=self.eval_factor(num1,f1)
        while self.i<len(self.s) and self.s[self.i]=='+':
            self.i+=1
            num2,f2=self.parse_factor()
            perm2=self.eval_factor(num2,f2)
            perm=compose_perm(perm, perm2)
        return perm

    def parse_expr(self):
        # 今の文法は termだけで良い
        return self.parse_term()

    def eval_factor(self,num,f):
        # numは繰り返し回数
        # fは部品名か部分式 (string or permutation)
        if isinstance(f,str):
            base=part_perm[f]
        else:
            base=f
        return perm_power(base,num)

def compose_perm(p1,p2):
    # p1,p2は長さNの順列。p1適用後p2適用
    # すなわち、x→p1[x]→p2[p1[x]]
    # compose_perm(p1,p2)[x] = p2[p1[x]]
    return [p2[p1[i]] for i in range(N)]

def perm_power(perm,k):
    # 置換permをk回合成
    # kは10億まであり、繰り返し2乗法で高速計算する
    result=list(range(N))
    base=perm
    while k>0:
        if k&1:
            result=compose_perm(result, base)
        base=compose_perm(base, base)
        k>>=1
    return result

E=int(input())
exprs=[input().strip() for _ in range(E)]

for expr in exprs:
    parser=Parser(expr)
    perm=parser.parse_expr()
    # permは0-basedでi番目の元の数字をどこに送るか→下端の順列
    # 問題の出力は、下端の各縦棒に付けられた番号を左から出力
    # つまり、下端の位置 0..N-1 がどの数字になったか?
    # permはtop端の位置iを下端のどこに移すかなので
    # perm[i]=下端のpos

    # 下端の位置から数字を出すには逆順列を書く
    inv=[0]*N
    for i,v in enumerate(perm):
        inv[v]=i
    print(*[x+1 for x in inv])