#標準入力
a,b = map(int,input().split())

#ドレスの数とパーティーの数が同じであればbをaで割った商を出力する
if b % a == 0:print(b // a)

#でなければbをaで割った商に1を足した値を出力する
else:print(b // a + 1)