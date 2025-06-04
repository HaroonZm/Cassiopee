import sys  # sysモジュールをインポート。システムに関する機能を利用できるようにする。
import fractions  # fractionsモジュールをインポート。有理数計算や最大公約数の計算などができる。

# 再帰関数（関数が自分自身を呼び出す関数）の再帰の深さ（何回まで呼び出せるか）を指定している。
# デフォルト値だと浅いため、10**6 すなわち100万回までに増やしている。
sys.setrecursionlimit(10 ** 6)

# "to_index"は無名関数（lambda式）として定義されている。
# 入力xを整数型（int）に変換して、そこから1を引いた値を返している。
# これは多くのプログラムで、1始まりの番号（例: 1,2,3...）を0始まり（例: 0,1,2...）に変換するためによく使われる。
to_index = lambda x: int(x) - 1

# "print_list_in_2D"はリスト（例えば2次元リストなど）を、各要素を改行（\n）で区切って表示する無名関数。
# *x はアンパック演算子で、xの各要素を個別の引数としてprintに渡す。
# sep="\n" はprintが要素間に何を挟むか指定していて、ここでは改行を挟むように指定している。
print_list_in_2D = lambda x: print(*x, sep="\n")

# 1行の入力を受け取り、int()で整数に変換して返す関数。
# たとえば、ユーザーが"4"と入力すると、4（整数型）が返る。
def input_int():
    return int(input())

# 1行の入力を受け取り、各文字（もしくは半角スペースで区切られていない1文字ずつ）をint()で整数に変換し、イテレータで返す。
# 例： "123"→ [1,2,3] のようになる。input()は文字列を返すので、map(int, input())で一文字ずつintに変換される。
def map_int_input():
    return map(int, input())

# より短い名前のエイリアスとして、map_int_inputをMIIと命名。
MII = map_int_input

# 1行の入力を受け取り、空白で区切って分割（split）し、それぞれ整数(int)に変換してイテレータで返す関数。
# 例えば "10 20" という入力だと、map(int, ["10","20"]) → [10, 20] となる。
def MII_split():
    return map(int, input().split())

# 入力された値をto_indexで変換する。
# 一文字か一つの入力を受けて、それをintに変換し1を引く、をすべての要素に適用している。
def MII_to_index():
    return map(to_index, input())

# 複数値を空白区切りで入力し、それぞれをto_index（int変換＋1引く）してイテレータで返す関数。
def MII_split_to_index():
    return map(to_index, input().split())

# 入力された全ての文字を整数へ変換しリスト化して返す関数。
# 例: 入力が"123"だと[1,2,3]になる。
def list_int_inputs():
    return list(map(int, input()))

# こちらは短縮形としてLIIと別名を付けている。
LII = list_int_inputs

# 空白区切りで複数個の値を入力し、各値を整数に変換、さらにリスト化して返す関数。
# 例: 入力が"1 2 3"だと[1,2,3]になる。
def LII_split():
    return list(map(int, input().split()))

# 指定した行数分（rows_number）だけ、LII()でリストを作り、それらをリスト化して2次元リストを作る関数。
# 例えば行数3なら[LII(), LII(), LII()]となる。
def LII_2D(rows_number):
    return [LII() for _ in range(rows_number)]

# 指定した行数分、各行を空白区切りで整数リスト（LII_split）として読み、2次元リストとしてまとめる関数。
def LII_split_2D(rows_number):
    return [LII_split() for _ in range(rows_number)]

# 2つの整数x, yの最小公倍数（lcm: least common multiple）を計算する関数。
# まずxとyを掛け算し、それを2つの値の最大公約数で割ることで求めている。
# max公約数はfractions.gcd(x, y)で求めている。
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

# ここで、ユーザーから2つの整数値を空白区切りで入力して受け取り、それらをそれぞれA, Bに格納する。
A, B = MII_split()

# 先ほど定義したlcm関数でAとBの最小公倍数を求め、そのまま画面に出力している。
print(lcm(A, B))