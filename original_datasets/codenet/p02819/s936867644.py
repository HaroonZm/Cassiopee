def P(n):#素数判定のアルゴリズム(O(√n))
    if type(n)!=int:raise TypeError#自然数以外はエラーを返す
    if n<1:raise ValueError#1未満は定義域を外れています
    if n==1:return -1#1は素数でも合成数でもないので負数を返す
    if n%2==0and n!=2:return 2#高速化用に2を別で判定
    a=3
    while a*a<n:#nの平方根以下のすべての奇数で割れるか判定
        if n%a==0:return a#割り切れたら最小の素因数を返す
        a+=2#奇数のみの判定なので偶数を飛ばせる
    return 0#割れなかったら(素数なら)0を返す
import math
a=int(input())
while P(a):a+=1
print(a)