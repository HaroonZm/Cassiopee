#成績の差が最も小さい 2 人を選ぶプログラム

#1 行目には学生の人数 n (2 ≤ n ≤ 1000)
#2 行目には　 ai（1 ≤ i ≤ n）が i 番目の学生の成績
while True:
 #1行目nを読み込む
  n =int(input())
  #もしn==0ならbreak
  if n==0:
    break
  else :
     #配列a[i]を読み込む(1<=i<=n)
    a = sorted(list(map(int, input().strip().split())))
    
    a_sub = 1000000
    for i in range(n-1):
      if abs(a[i]-a[i+1]) < a_sub :
        a_sub =  abs(a[i]-a[i+1])
    print(a_sub)