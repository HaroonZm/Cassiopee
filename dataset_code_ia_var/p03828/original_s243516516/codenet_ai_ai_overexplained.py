# mathモジュールをインポートします
# これにより、平方根や階乗などの数学的な関数が使えるようになります
import math

# input()は標準入力から文字列を受け取ります
# int()は文字列を整数型に変換します
# 例えば、ユーザーが「5」と入力した場合、xは整数5になります
x = int(input())

# 階乗を計算します
# math.factorial(x)は、xの階乗つまり1からxまでのすべての整数を掛けた値を返します
# 例: x=5の場合、aには120が代入されます(5*4*3*2*1)
a = math.factorial(x)

# 素数判定関数の定義
# 素数とは1とその数自身以外に約数を持たない2以上の整数です
# is_prime_2という関数名です。引数numの値が素数であればTrue、そうでなければFalseを返します
def is_prime_2(num):
    # numが2未満の場合は素数ではないのでFalseを返します
    if num < 2:
        return False
    # 2, 3, 5はいずれも素数なのでTrueを返します
    if num == 2 or num == 3 or num == 5:
        return True
    # 2, 3, 5のいずれかで割り切れる場合は素数ではないのでFalseを返します
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    # ここから先は上記でふるい落とされなかった数に限ります
    # まず先頭の判定で使用された2,3,5を除いた数(7以上)で判定していきます
    # 例えば7,11,13,...でnumを割り切れるかを調べます。
    # primeは現在試している割る数（候補となる素数）で、最初は7から始まります
    prime = 7
    # step変数は、次に調べる素数候補までの間隔を制御します
    # 7の次の素数は11なので+4、11の次は13なので+2、という交互なパターンに合わせています
    step = 4
    # num_sqrtはnumの平方根です. それより大きい数で割る必要はありません
    # なぜならa*b=numとして、aとbが両方平方根より大きいとnumより大きくなるため
    num_sqrt = math.sqrt(num)
    # while文でprime（割る数）が平方根以下であれば繰り返します
    while prime <= num_sqrt:
        # numがprimeで割り切れる場合は素数ではないためFalseを返します
        if num % prime == 0:
            return False
        # primeをstep分増やします
        prime += step
        # stepは4→2→4→2...と交互になります(素数の間隔のため)
        step = 6 - step
    # すべての判定をクリアした場合は素数なのでTrueを返します
    return True

# x以下のすべての整数について素数かどうか判定し、素数リストを作ります
# sosu_listは日本語で「素数リスト」という意味です
sosu_list = []
# 0からxまで（xを含む）繰り返します
for i in range(x+1):
    # is_prime_2でiが素数か判定します
    if is_prime_2(i):
        # 素数の場合だけリストに追加します
        sosu_list.append(i)

# 次に、aを素因数分解します
# aはx!です。aを割ることで、aを構成する素数の指数を求めます
# sosu_cntという辞書を使って、素数ごとに使われた回数（指数）をカウントします
sosu_cnt = {}
# sosu_list(素数リスト)の各素数について調べます
for sosu in sosu_list:
    # aがsosuで割り切れる限り繰り返します
    while a % sosu == 0:
        # すでに辞書にsosuが登録されていれば値を1増やし、そうでなければ初期値1を設定します
        if sosu in sosu_cnt:
            sosu_cnt[sosu] += 1
        else:
            sosu_cnt[sosu] = 1
        # aをsosuで割った値に更新します。//は整数除算です
        a //= sosu

# 次に、素数ごとの個数＋1をかけあわせて約数の総数を計算します
# 全ての約数の個数をans（answerの略）に入れます
ans = 1
# sosu_cnt.items()で(素数,個数)のペアを一つずつ取り出します
for key, value in sosu_cnt.items():
    # 約数の個数を求めるにはそれぞれの指数に1を足してかけ合わせます
    # 例えば60=2^2*3^1*5^1の場合、(2+1)*(1+1)*(1+1)=3*2*2=12通り
    sosu_cnt[key] += 1
    # ansに掛け合わせます。巨大な値になるので10^9+7で割った余りを取ります（よく使われる大きな素数です）
    ans = (ans * sosu_cnt[key]) % (10 ** 9 + 7)
# 最終的な答えを出力します
print(ans)